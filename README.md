# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_10:03:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,959 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 10:03:19 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-27 10:03:03 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.040 |  |
| 2026-11-27 10:02:57 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:02:55 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.000 |  |
| 2026-11-27 10:02:49 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.073 |  |
| 2026-11-27 10:02:44 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | -0.040 |  |
| 2026-11-27 10:02:39 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.122 |  |
| 2026-11-27 10:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:02:17 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-27 10:02:13 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | 0.000 |  |
| 2026-11-27 10:02:09 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.062 |  |
| 2026-11-27 10:01:48 | Magura (Kalu Ganga) | 4.36 | 🟡 Alert | -0.129 |  |
| 2026-11-27 10:01:43 | Thanamalwila (Kirindi Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:01:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-11-27 10:01:29 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.059 |  |
| 2026-11-27 10:01:08 | Moraketiya (Walawe Ganga) | 3.77 | 🟡 Alert | -0.032 |  |
| 2026-11-27 10:00:48 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:00:36 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 10:02:55 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.000 |  |
| 2026-11-27 10:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | 0.000 |  |
| 2026-11-27 10:01:08 | Moraketiya (Walawe Ganga) | 3.77 | 🟡 Alert | -0.032 |  |
| 2026-11-27 10:01:48 | Magura (Kalu Ganga) | 4.36 | 🟡 Alert | -0.129 |  |
| 2026-11-27 09:03:49 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-27 10:02:17 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-27 09:05:54 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-27 09:07:34 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-27 09:09:41 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 10:00:48 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 09:05:31 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-27 09:03:21 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:03:19 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-27 10:01:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-11-27 09:15:44 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.018 |  |
| 2026-11-27 10:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:02:57 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:02:13 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | -0.020 |  |
| 2026-11-27 09:03:57 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:01:43 | Thanamalwila (Kirindi Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-11-27 09:02:22 | Moragaswewa (Deduru Oya) | 3.48 | 🟢 Normal | -0.021 |  |
| 2026-11-27 09:04:21 | Galgamuwa (Mee Oya) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-11-27 09:08:11 | Badalgama (Maha Oya) | 4.94 | 🟢 Normal | -0.030 |  |
| 2026-11-27 10:00:36 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.030 |  |
| 2026-11-27 10:03:03 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.040 |  |
| 2026-11-27 10:02:44 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | -0.040 |  |
| 2026-11-27 09:00:23 | Kuda Oya (Kirindi Oya) | 2.66 | 🟢 Normal | -0.052 |  |
| 2026-11-27 10:01:29 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.059 |  |
| 2026-11-27 09:07:57 | Holombuwa (Kelani Ganga) | 1.62 | 🟢 Normal | -0.059 |  |
| 2026-11-27 10:02:09 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.062 |  |
| 2026-11-27 09:05:13 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.066 |  |
| 2026-11-27 09:04:33 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.073 |  |
| 2026-11-27 10:02:49 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.073 |  |
| 2026-11-27 09:04:04 | Peradeniya (Mahaweli Ganga) | 3.92 | 🟢 Normal | -0.084 |  |
| 2026-11-27 09:05:52 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.087 |  |
| 2026-11-27 09:03:18 | Siyambalanduwa (Heda Oya) | 1.39 | 🟢 Normal | -0.088 |  |
| 2026-11-27 09:04:25 | Giriulla (Maha Oya) | 4.02 | 🟢 Normal | -0.120 |  |
| 2026-11-27 10:02:39 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.122 |  |
| 2026-11-27 09:03:33 | Thawalama (Gin Ganga) | 2.51 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)