# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_18:13:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,401 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 18:13:37 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-10-29 18:11:11 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:09:05 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:07:26 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | -0.029 |  |
| 2026-10-29 18:06:40 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:06:21 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-10-29 18:05:14 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.020 |  |
| 2026-10-29 18:05:01 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-29 18:05:00 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:04:47 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:04:13 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-29 18:04:00 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.113 |  |
| 2026-10-29 18:03:50 | Rathnapura (Kalu Ganga) | 4.40 | 🟢 Normal | -0.030 |  |
| 2026-10-29 18:03:31 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-10-29 18:03:21 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-29 18:03:04 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:02:39 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.040 |  |
| 2026-10-29 18:02:34 | Baddegama (Gin Ganga) | 3.96 | 🟡 Alert | -0.033 |  |
| 2026-10-29 18:02:26 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:02:25 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:02:20 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-29 18:02:19 | Ellagawa (Kalu Ganga) | 9.77 | 🟢 Normal | -0.030 |  |
| 2026-10-29 18:02:15 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:02:07 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-29 18:01:50 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-10-29 18:01:49 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.059 |  |
| 2026-10-29 18:01:34 | Dunamale (Aththanagalu Oya) | 2.37 | 🟢 Normal | -0.020 |  |
| 2026-10-29 18:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:01:33 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.14 | 🟠 Minor Flood | -0.023 |  |
| 2026-10-29 18:01:28 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.031 |  |
| 2026-10-29 18:01:25 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-29 18:01:22 | Putupaula (Kalu Ganga) | 3.66 | 🟡 Alert | -0.011 |  |
| 2026-10-29 18:01:17 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:01:05 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:01:00 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-29 18:00:44 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 18:00:29 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:00:29 | Magura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 18:00:44 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 18:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.14 | 🟠 Minor Flood | -0.023 |  |
| 2026-10-29 18:13:37 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-10-29 18:01:22 | Putupaula (Kalu Ganga) | 3.66 | 🟡 Alert | -0.011 |  |
| 2026-10-29 18:02:34 | Baddegama (Gin Ganga) | 3.96 | 🟡 Alert | -0.033 |  |
| 2026-10-29 18:05:01 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-29 18:04:13 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-29 18:02:07 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-29 18:01:25 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-29 18:03:21 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-29 18:02:20 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-29 18:05:00 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:01:17 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:01:33 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:11:11 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:02:26 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:09:05 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:00:29 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:01:05 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:04:47 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:03:04 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:06:40 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:02:25 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:02:15 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-29 18:06:21 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-10-29 18:01:00 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-29 18:03:31 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-10-29 18:05:14 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.020 |  |
| 2026-10-29 18:01:34 | Dunamale (Aththanagalu Oya) | 2.37 | 🟢 Normal | -0.020 |  |
| 2026-10-29 18:01:50 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-10-29 18:07:26 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | -0.029 |  |
| 2026-10-29 18:03:50 | Rathnapura (Kalu Ganga) | 4.40 | 🟢 Normal | -0.030 |  |
| 2026-10-29 18:02:19 | Ellagawa (Kalu Ganga) | 9.77 | 🟢 Normal | -0.030 |  |
| 2026-10-29 18:01:28 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.031 |  |
| 2026-10-29 18:00:29 | Magura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.040 |  |
| 2026-10-29 18:02:39 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.040 |  |
| 2026-10-29 18:01:49 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.059 |  |
| 2026-10-29 18:04:00 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)