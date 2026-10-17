# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_23:10:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,769 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Norwood — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 23:10:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.46 | 🟡 Alert | -0.019 |  |
| 2026-10-17 23:08:28 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-10-17 23:08:24 | Thawalama (Gin Ganga) | 3.69 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-10-17 23:07:56 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:07:11 | Putupaula (Kalu Ganga) | 2.07 | 🟢 Normal | -0.009 |  |
| 2026-10-17 23:07:04 | Holombuwa (Kelani Ganga) | 2.16 | 🟢 Normal | -0.526 |  |
| 2026-10-17 23:06:54 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-10-17 23:06:21 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -16.000 |  |
| 2026-10-17 23:05:59 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | 45.000 | 🔺 Rising |
| 2026-10-17 23:05:55 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 45.000 | 🔺 Rising |
| 2026-10-17 23:05:13 | Urawa (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-17 23:05:01 | Pitabeddara (Nilwala Ganga) | 3.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 23:04:58 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-10-17 23:04:52 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-10-17 23:04:37 | Horowpothana (Yan Oya) | 2.82 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-17 23:04:22 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.412 |  |
| 2026-10-17 23:04:16 | Dunamale (Aththanagalu Oya) | 2.77 | 🟢 Normal | -0.030 |  |
| 2026-10-17 23:04:02 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.033 |  |
| 2026-10-17 23:03:56 | Thaldena (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.202 |  |
| 2026-10-17 23:03:48 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-17 23:03:38 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 23:03:34 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-17 23:03:11 | Rathnapura (Kalu Ganga) | 6.17 | 🟡 Alert | -0.128 |  |
| 2026-10-17 23:03:04 | Panadugama (Nilwala Ganga) | 6.18 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-10-17 23:03:00 | Glencourse (Kelani Ganga) | 13.30 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-10-17 23:02:38 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | -0.024 |  |
| 2026-10-17 23:02:36 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | -16.000 |  |
| 2026-10-17 23:02:34 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-17 23:02:23 | Norwood (Kelani Ganga) | 1.60 | 🟡 Alert | -0.061 |  |
| 2026-10-17 23:02:17 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:02:10 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | -0.847 |  |
| 2026-10-17 23:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.226 |  |
| 2026-10-17 23:01:50 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:01:40 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:01:34 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 23:01:24 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.158 |  |
| 2026-10-17 23:00:51 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:00:12 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.256 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 23:03:04 | Panadugama (Nilwala Ganga) | 6.18 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-10-17 23:03:38 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 23:10:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.46 | 🟡 Alert | -0.019 |  |
| 2026-10-17 23:02:23 | Norwood (Kelani Ganga) | 1.60 | 🟡 Alert | -0.061 |  |
| 2026-10-17 23:03:11 | Rathnapura (Kalu Ganga) | 6.17 | 🟡 Alert | -0.128 |  |
| 2026-10-17 23:05:59 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | 45.000 | 🔺 Rising |
| 2026-10-17 23:08:28 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-10-17 23:00:12 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-10-17 23:08:24 | Thawalama (Gin Ganga) | 3.69 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-10-17 23:03:00 | Glencourse (Kelani Ganga) | 13.30 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-10-17 23:04:52 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-10-17 23:03:48 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-17 23:04:37 | Horowpothana (Yan Oya) | 2.82 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-17 23:05:13 | Urawa (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-17 23:03:34 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-17 23:01:34 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 23:05:01 | Pitabeddara (Nilwala Ganga) | 3.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:02:17 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:01:50 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:00:51 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:07:56 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:01:40 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:07:11 | Putupaula (Kalu Ganga) | 2.07 | 🟢 Normal | -0.009 |  |
| 2026-10-17 21:21:56 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-10-17 23:02:34 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-17 23:06:54 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-10-17 23:02:38 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | -0.024 |  |
| 2026-10-17 23:04:58 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-10-17 23:04:16 | Dunamale (Aththanagalu Oya) | 2.77 | 🟢 Normal | -0.030 |  |
| 2026-10-17 23:04:02 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.033 |  |
| 2026-10-17 18:01:56 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.040 |  |
| 2026-10-17 23:01:24 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.158 |  |
| 2026-10-17 23:03:56 | Thaldena (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.202 |  |
| 2026-10-17 23:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.226 |  |
| 2026-10-17 23:04:22 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.412 |  |
| 2026-10-17 23:07:04 | Holombuwa (Kelani Ganga) | 2.16 | 🟢 Normal | -0.526 |  |
| 2026-10-17 23:02:10 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | -0.847 |  |
| 2026-10-17 23:06:21 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -16.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)