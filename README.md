# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_22:19:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,931 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Pitabeddara — Alert; 🟡 Thawalama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 22:19:49 | Ellagawa (Kalu Ganga) | 7.77 | 🟢 Normal | -0.025 |  |
| 2026-10-15 22:15:55 | Magura (Kalu Ganga) | 3.88 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-15 22:14:08 | Dunamale (Aththanagalu Oya) | 3.81 | 🟡 Alert | 0.008 | 🔺 Rising |
| 2026-10-15 22:11:48 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-15 22:11:07 | Baddegama (Gin Ganga) | 2.81 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-15 22:08:59 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-10-15 22:08:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | -0.029 |  |
| 2026-10-15 22:08:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:08:32 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-15 22:08:10 | Thawalama (Gin Ganga) | 4.06 | 🟡 Alert | 0.000 |  |
| 2026-10-15 22:07:45 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:06:35 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:06:33 | Norwood (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 22:06:21 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 22:05:46 | Urawa (Nilwala Ganga) | 2.67 | 🟡 Alert | -0.049 |  |
| 2026-10-15 22:05:40 | Pitabeddara (Nilwala Ganga) | 4.76 | 🟡 Alert | 0.000 |  |
| 2026-10-15 22:05:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-10-15 22:05:24 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | -0.053 |  |
| 2026-10-15 22:05:04 | Panadugama (Nilwala Ganga) | 6.48 | 🟠 Minor Flood | 0.066 | 🔺 Rising |
| 2026-10-15 22:05:04 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:04:35 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-15 22:04:19 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:04:18 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:04:15 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | -0.030 |  |
| 2026-10-15 22:03:31 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-15 22:03:19 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:02:40 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 22:02:39 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.106 |  |
| 2026-10-15 22:02:38 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.040 |  |
| 2026-10-15 22:02:10 | Moraketiya (Walawe Ganga) | 2.25 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-15 22:02:10 | Moragaswewa (Deduru Oya) | 2.63 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-15 22:02:01 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 22:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 22:01:04 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-15 22:00:48 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:00:39 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 22:05:04 | Panadugama (Nilwala Ganga) | 6.48 | 🟠 Minor Flood | 0.066 | 🔺 Rising |
| 2026-10-15 22:01:04 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-15 22:14:08 | Dunamale (Aththanagalu Oya) | 3.81 | 🟡 Alert | 0.008 | 🔺 Rising |
| 2026-10-15 22:05:40 | Pitabeddara (Nilwala Ganga) | 4.76 | 🟡 Alert | 0.000 |  |
| 2026-10-15 22:08:10 | Thawalama (Gin Ganga) | 4.06 | 🟡 Alert | 0.000 |  |
| 2026-10-15 22:08:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | -0.029 |  |
| 2026-10-15 22:05:46 | Urawa (Nilwala Ganga) | 2.67 | 🟡 Alert | -0.049 |  |
| 2026-10-15 22:02:10 | Moragaswewa (Deduru Oya) | 2.63 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-15 22:08:32 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-15 22:03:31 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-15 22:02:10 | Moraketiya (Walawe Ganga) | 2.25 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-15 22:04:35 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-15 22:15:55 | Magura (Kalu Ganga) | 3.88 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-15 22:11:07 | Baddegama (Gin Ganga) | 2.81 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-15 22:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 22:06:21 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 22:02:01 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 18:18:48 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-15 22:11:48 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-15 22:02:40 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 22:06:33 | Norwood (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 22:04:19 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:07:45 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:00:48 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:08:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:00:39 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:05:04 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:04:18 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:03:19 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:06:35 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:08:59 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-10-15 22:19:49 | Ellagawa (Kalu Ganga) | 7.77 | 🟢 Normal | -0.025 |  |
| 2026-10-15 22:04:15 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | -0.030 |  |
| 2026-10-15 22:02:38 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.040 |  |
| 2026-10-15 22:05:24 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | -0.053 |  |
| 2026-10-15 22:05:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-10-15 22:02:39 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)