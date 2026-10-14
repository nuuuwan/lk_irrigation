# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_11:07:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,584 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 11:07:40 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:07:23 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:06:56 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.061 |  |
| 2026-10-14 11:06:28 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 11:06:11 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:05:46 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-14 11:04:47 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-10-14 11:04:35 | Putupaula (Kalu Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-10-14 11:04:15 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:03:36 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-14 11:03:34 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | -0.030 |  |
| 2026-10-14 11:03:30 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.063 |  |
| 2026-10-14 11:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.76 | 🟡 Alert | 0.143 | 🔺 Rising |
| 2026-10-14 11:03:22 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-14 11:03:16 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.016 |  |
| 2026-10-14 11:03:11 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.020 |  |
| 2026-10-14 11:02:52 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:02:51 | Panadugama (Nilwala Ganga) | 5.91 | 🟡 Alert | -0.029 |  |
| 2026-10-14 11:02:42 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | -0.031 |  |
| 2026-10-14 11:02:40 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:02:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:02:27 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.021 |  |
| 2026-10-14 11:02:21 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.030 |  |
| 2026-10-14 11:02:09 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-10-14 11:02:06 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.013 |  |
| 2026-10-14 11:01:43 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-14 11:01:42 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:01:27 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-14 11:01:26 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:01:12 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:01:03 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-14 11:01:02 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-10-14 10:26:07 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 10:17:37 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 11:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.76 | 🟡 Alert | 0.143 | 🔺 Rising |
| 2026-10-14 11:02:51 | Panadugama (Nilwala Ganga) | 5.91 | 🟡 Alert | -0.029 |  |
| 2026-10-14 10:06:53 | Magura (Kalu Ganga) | 5.31 | 🟡 Alert | -0.052 |  |
| 2026-10-14 11:03:22 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-14 11:06:28 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 11:06:11 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:02:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:07:23 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:07:40 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:01:01 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:01:42 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:15:04 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:02:52 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:01:12 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:01:26 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:02:06 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:19:20 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:04:15 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-14 11:03:36 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-14 11:01:43 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-14 11:01:03 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-14 11:05:46 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-14 11:02:09 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-10-14 11:01:27 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-14 11:01:02 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-10-14 11:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.013 |  |
| 2026-10-14 11:03:16 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.016 |  |
| 2026-10-14 10:12:54 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.019 |  |
| 2026-10-14 11:03:11 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.020 |  |
| 2026-10-14 11:04:47 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-10-14 11:04:35 | Putupaula (Kalu Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-10-14 11:02:27 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.021 |  |
| 2026-10-14 11:03:34 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | -0.030 |  |
| 2026-10-14 11:02:21 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.030 |  |
| 2026-10-14 11:02:42 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | -0.031 |  |
| 2026-10-14 11:06:56 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.061 |  |
| 2026-10-14 11:03:30 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.063 |  |
| 2026-10-14 10:09:16 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)