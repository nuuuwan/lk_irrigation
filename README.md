# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_04:22:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,839 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 04:22:20 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-10-19 04:08:36 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.019 |  |
| 2026-10-19 04:07:41 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-19 04:07:30 | Hanwella (Kelani Ganga) | 3.83 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-19 04:07:28 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | -0.009 |  |
| 2026-10-19 04:07:27 | Rathnapura (Kalu Ganga) | 3.94 | 🟢 Normal | -0.133 |  |
| 2026-10-19 04:06:16 | Norwood (Kelani Ganga) | 1.46 | 🟢 Normal | -0.067 |  |
| 2026-10-19 04:04:51 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-10-19 04:04:44 | Glencourse (Kelani Ganga) | 11.74 | 🟢 Normal | -0.171 |  |
| 2026-10-19 04:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | -0.057 |  |
| 2026-10-19 04:04:06 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.182 |  |
| 2026-10-19 04:04:03 | Dunamale (Aththanagalu Oya) | 2.13 | 🟢 Normal | -0.022 |  |
| 2026-10-19 04:04:01 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.061 |  |
| 2026-10-19 04:03:37 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:03:09 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:03:01 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | -0.091 |  |
| 2026-10-19 04:02:47 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:02:46 | Thalgahagoda (Nilwala Ganga) | 1.99 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-19 04:02:16 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.060 |  |
| 2026-10-19 04:02:08 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-10-19 04:02:07 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-19 04:02:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-19 04:01:53 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 04:01:49 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-10-19 04:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-19 04:01:48 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:01:44 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.050 |  |
| 2026-10-19 04:01:38 | Ellagawa (Kalu Ganga) | 7.33 | 🟢 Normal | -0.036 |  |
| 2026-10-19 04:01:20 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-10-19 04:01:00 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.021 |  |
| 2026-10-19 04:00:51 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:00:19 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:54:13 | Putupaula (Kalu Ganga) | 1.73 | 🟢 Normal | -0.182 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 04:02:46 | Thalgahagoda (Nilwala Ganga) | 1.99 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-19 03:20:07 | Panadugama (Nilwala Ganga) | 5.65 | 🟡 Alert | -0.069 |  |
| 2026-10-19 04:02:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-19 04:02:07 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-19 04:07:30 | Hanwella (Kelani Ganga) | 3.83 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-19 04:01:53 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 03:05:18 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 04:00:19 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:02:47 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:03:09 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:01:48 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:00:51 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:03:37 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:07:28 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | -0.009 |  |
| 2026-10-19 04:07:41 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-19 04:04:51 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-19 04:01:20 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-10-19 04:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-19 04:22:20 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-10-19 04:08:36 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.019 |  |
| 2026-10-19 04:01:00 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.021 |  |
| 2026-10-19 04:02:08 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-10-19 03:05:08 | Baddegama (Gin Ganga) | 2.82 | 🟢 Normal | -0.021 |  |
| 2026-10-19 04:04:03 | Dunamale (Aththanagalu Oya) | 2.13 | 🟢 Normal | -0.022 |  |
| 2026-10-19 03:12:41 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.027 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-19 04:01:38 | Ellagawa (Kalu Ganga) | 7.33 | 🟢 Normal | -0.036 |  |
| 2026-10-19 04:01:49 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |
| 2026-10-19 04:01:44 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.050 |  |
| 2026-10-19 04:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | -0.057 |  |
| 2026-10-19 04:02:16 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.060 |  |
| 2026-10-19 04:04:01 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.061 |  |
| 2026-10-19 04:06:16 | Norwood (Kelani Ganga) | 1.46 | 🟢 Normal | -0.067 |  |
| 2026-10-19 04:03:01 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | -0.091 |  |
| 2026-10-19 04:07:27 | Rathnapura (Kalu Ganga) | 3.94 | 🟢 Normal | -0.133 |  |
| 2026-10-19 04:04:44 | Glencourse (Kelani Ganga) | 11.74 | 🟢 Normal | -0.171 |  |
| 2026-10-19 04:04:06 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)