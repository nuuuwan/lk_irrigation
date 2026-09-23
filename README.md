# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_07:28:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,547 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 07:28:35 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | -0.034 |  |
| 2026-09-23 07:13:51 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.051 |  |
| 2026-09-23 07:11:20 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:10:45 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:10:23 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:09:07 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.038 |  |
| 2026-09-23 07:08:36 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-09-23 07:08:28 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.045 |  |
| 2026-09-23 07:08:26 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-09-23 07:07:36 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:07:19 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.019 |  |
| 2026-09-23 07:07:11 | Glencourse (Kelani Ganga) | 12.89 | 🟢 Normal | -0.020 |  |
| 2026-09-23 07:06:50 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:06:23 | Peradeniya (Mahaweli Ganga) | 3.33 | 🟢 Normal | -0.091 |  |
| 2026-09-23 07:06:01 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | -0.038 |  |
| 2026-09-23 07:05:59 | Rathnapura (Kalu Ganga) | 3.91 | 🟢 Normal | -0.020 |  |
| 2026-09-23 07:05:56 | Ellagawa (Kalu Ganga) | 8.24 | 🟢 Normal | -0.028 |  |
| 2026-09-23 07:05:39 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:05:25 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:05:17 | Baddegama (Gin Ganga) | 3.90 | 🟡 Alert | -0.021 |  |
| 2026-09-23 07:05:04 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:04:38 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-23 07:04:29 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:04:07 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-09-23 07:03:47 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.069 |  |
| 2026-09-23 07:03:38 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-23 07:03:00 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:02:57 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:02:41 | Deraniyagala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.232 |  |
| 2026-09-23 07:02:39 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:02:12 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:02:12 | Kithulgala (Kelani Ganga) | 2.46 | 🟢 Normal | -0.052 |  |
| 2026-09-23 07:01:57 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 07:01:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:01:47 | Magura (Kalu Ganga) | 4.09 | 🟡 Alert | -0.020 |  |
| 2026-09-23 07:01:31 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:01:13 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:01:07 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:00:50 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.020 |  |
| 2026-09-23 07:00:33 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 07:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-23 07:01:47 | Magura (Kalu Ganga) | 4.09 | 🟡 Alert | -0.020 |  |
| 2026-09-23 07:05:17 | Baddegama (Gin Ganga) | 3.90 | 🟡 Alert | -0.021 |  |
| 2026-09-23 07:28:35 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | -0.034 |  |
| 2026-09-23 07:01:57 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 07:04:38 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-23 07:03:38 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:02:57 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:05:25 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:01:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:01:07 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:05:04 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:06:50 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:10:45 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:07:36 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:01:13 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:02:39 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:01:31 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:04:29 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:03:00 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:05:39 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:11:20 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:02:12 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:08:36 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-09-23 07:08:26 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-09-23 07:07:19 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.019 |  |
| 2026-09-23 07:00:50 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.020 |  |
| 2026-09-23 07:07:11 | Glencourse (Kelani Ganga) | 12.89 | 🟢 Normal | -0.020 |  |
| 2026-09-23 07:05:59 | Rathnapura (Kalu Ganga) | 3.91 | 🟢 Normal | -0.020 |  |
| 2026-09-23 07:05:56 | Ellagawa (Kalu Ganga) | 8.24 | 🟢 Normal | -0.028 |  |
| 2026-09-23 07:04:07 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-09-23 07:06:01 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | -0.038 |  |
| 2026-09-23 07:09:07 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.038 |  |
| 2026-09-23 07:08:28 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.045 |  |
| 2026-09-23 07:13:51 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.051 |  |
| 2026-09-23 07:02:12 | Kithulgala (Kelani Ganga) | 2.46 | 🟢 Normal | -0.052 |  |
| 2026-09-23 07:03:47 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.069 |  |
| 2026-09-23 07:06:23 | Peradeniya (Mahaweli Ganga) | 3.33 | 🟢 Normal | -0.091 |  |
| 2026-09-23 07:02:41 | Deraniyagala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.232 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)