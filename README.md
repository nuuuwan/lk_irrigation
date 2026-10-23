# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_09:25:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,651 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 09:25:06 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.017 |  |
| 2026-10-23 09:16:44 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-23 09:15:09 | Ellagawa (Kalu Ganga) | 7.67 | 🟢 Normal | -0.024 |  |
| 2026-10-23 09:11:55 | Horowpothana (Yan Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:11:46 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | -0.052 |  |
| 2026-10-23 09:11:35 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | -0.042 |  |
| 2026-10-23 09:09:23 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-10-23 09:08:01 | Badalgama (Maha Oya) | 3.58 | 🟢 Normal | -0.040 |  |
| 2026-10-23 09:07:36 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:05:46 | Rathnapura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.129 |  |
| 2026-10-23 09:05:39 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.039 |  |
| 2026-10-23 09:04:54 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-10-23 09:04:51 | Galgamuwa (Mee Oya) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-10-23 09:03:51 | Putupaula (Kalu Ganga) | 2.01 | 🟢 Normal | -0.039 |  |
| 2026-10-23 09:03:41 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:03:38 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-10-23 09:03:33 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:03:32 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.024 |  |
| 2026-10-23 09:03:31 | Dunamale (Aththanagalu Oya) | 2.78 | 🟢 Normal | -0.041 |  |
| 2026-10-23 09:03:28 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-10-23 09:03:14 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-10-23 09:02:58 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 09:02:58 | Moragaswewa (Deduru Oya) | 4.84 | 🟡 Alert | -0.030 |  |
| 2026-10-23 09:02:53 | Hanwella (Kelani Ganga) | 4.25 | 🟢 Normal | -0.071 |  |
| 2026-10-23 09:02:52 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:02:49 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-23 09:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-10-23 09:02:24 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-10-23 09:02:22 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.078 |  |
| 2026-10-23 09:02:04 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.041 |  |
| 2026-10-23 09:01:52 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:01:47 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-10-23 09:01:45 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-23 09:01:20 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:01:14 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.072 |  |
| 2026-10-23 09:01:14 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.080 |  |
| 2026-10-23 09:00:49 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-23 09:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 09:00:39 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 09:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-10-23 09:02:58 | Moragaswewa (Deduru Oya) | 4.84 | 🟡 Alert | -0.030 |  |
| 2026-10-23 09:00:49 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-23 09:02:58 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 09:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 09:00:39 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:01:20 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:11:55 | Horowpothana (Yan Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:03:41 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:02:52 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:03:33 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:01:52 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:07:36 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-23 09:16:44 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-23 09:01:45 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-23 09:02:49 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-23 09:03:28 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-10-23 09:02:24 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-10-23 09:25:06 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.017 |  |
| 2026-10-23 09:04:51 | Galgamuwa (Mee Oya) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-10-23 09:04:54 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-10-23 09:03:38 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-10-23 09:03:14 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-10-23 09:01:47 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-10-23 09:03:32 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.024 |  |
| 2026-10-23 09:15:09 | Ellagawa (Kalu Ganga) | 7.67 | 🟢 Normal | -0.024 |  |
| 2026-10-23 09:09:23 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-10-23 09:05:39 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.039 |  |
| 2026-10-23 09:03:51 | Putupaula (Kalu Ganga) | 2.01 | 🟢 Normal | -0.039 |  |
| 2026-10-23 09:08:01 | Badalgama (Maha Oya) | 3.58 | 🟢 Normal | -0.040 |  |
| 2026-10-23 09:03:31 | Dunamale (Aththanagalu Oya) | 2.78 | 🟢 Normal | -0.041 |  |
| 2026-10-23 09:02:04 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.041 |  |
| 2026-10-23 09:11:35 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | -0.042 |  |
| 2026-10-23 09:11:46 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | -0.052 |  |
| 2026-10-23 09:02:53 | Hanwella (Kelani Ganga) | 4.25 | 🟢 Normal | -0.071 |  |
| 2026-10-23 09:01:14 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.072 |  |
| 2026-10-23 09:02:22 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.078 |  |
| 2026-10-23 09:01:14 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.080 |  |
| 2026-10-23 09:05:46 | Rathnapura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)