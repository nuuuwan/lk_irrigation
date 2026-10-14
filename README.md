# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_07:10:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,429 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 07:10:50 | Thawalama (Gin Ganga) | 2.98 | 🟢 Normal | -0.186 |  |
| 2026-10-14 07:09:37 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.018 |  |
| 2026-10-14 07:09:20 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:07:43 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-14 07:07:21 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 07:06:34 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.019 |  |
| 2026-10-14 07:06:15 | Putupaula (Kalu Ganga) | 2.02 | 🟢 Normal | -0.028 |  |
| 2026-10-14 07:05:53 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:05:27 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-10-14 07:05:21 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | -0.096 |  |
| 2026-10-14 07:05:19 | Rathnapura (Kalu Ganga) | 4.11 | 🟢 Normal | -0.087 |  |
| 2026-10-14 07:05:13 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.129 |  |
| 2026-10-14 07:05:13 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.010 |  |
| 2026-10-14 07:05:08 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 07:04:39 | Magura (Kalu Ganga) | 5.41 | 🟡 Alert | -0.010 |  |
| 2026-10-14 07:04:14 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.028 |  |
| 2026-10-14 07:04:03 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:04:00 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:03:53 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-14 07:03:51 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 07:03:47 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | -0.020 |  |
| 2026-10-14 07:03:45 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-14 07:03:26 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-14 07:03:03 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:02:42 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.040 |  |
| 2026-10-14 07:02:42 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:02:35 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:02:08 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | 0.189 | 🔺 Rising |
| 2026-10-14 07:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-14 07:01:52 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:01:18 | Pitabeddara (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.321 |  |
| 2026-10-14 07:01:06 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-14 07:00:59 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 07:00:57 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:00:45 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:00:40 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 07:03:51 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 06:03:26 | Panadugama (Nilwala Ganga) | 6.04 | 🟠 Minor Flood | -0.030 |  |
| 2026-10-14 07:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | 0.189 | 🔺 Rising |
| 2026-10-14 07:04:39 | Magura (Kalu Ganga) | 5.41 | 🟡 Alert | -0.010 |  |
| 2026-10-14 07:01:06 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-14 07:03:53 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-14 07:03:26 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-14 07:05:08 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 07:03:45 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-14 07:07:21 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 07:00:59 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 07:02:35 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:00:57 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:01:52 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:04:03 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:09:20 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:02:08 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:02:42 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:09:16 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:05:53 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:03:03 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:04:00 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:00:40 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:00:45 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:05:13 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.010 |  |
| 2026-10-14 07:07:43 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-14 07:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-14 07:09:37 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.018 |  |
| 2026-10-14 07:06:34 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.019 |  |
| 2026-10-14 07:03:47 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | -0.020 |  |
| 2026-10-14 07:05:27 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-10-14 07:06:15 | Putupaula (Kalu Ganga) | 2.02 | 🟢 Normal | -0.028 |  |
| 2026-10-14 07:04:14 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.028 |  |
| 2026-10-14 07:02:42 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.040 |  |
| 2026-10-14 07:05:19 | Rathnapura (Kalu Ganga) | 4.11 | 🟢 Normal | -0.087 |  |
| 2026-10-14 07:05:21 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | -0.096 |  |
| 2026-10-14 07:05:13 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.129 |  |
| 2026-10-14 07:10:50 | Thawalama (Gin Ganga) | 2.98 | 🟢 Normal | -0.186 |  |
| 2026-10-14 07:01:18 | Pitabeddara (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.321 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)