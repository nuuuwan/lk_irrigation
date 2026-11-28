# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_20:24:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **328,260 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 20:24:29 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:17:49 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-11-28 20:15:36 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-28 20:13:21 | Thalgahagoda (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 20:12:15 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-28 20:10:00 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-11-28 20:09:49 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 20:07:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.000 |  |
| 2026-11-28 20:07:05 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-28 20:06:39 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.069 |  |
| 2026-11-28 20:06:35 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:06:00 | Panadugama (Nilwala Ganga) | 5.17 | 🟡 Alert | 0.088 | 🔺 Rising |
| 2026-11-28 20:04:52 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-28 20:04:44 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.040 |  |
| 2026-11-28 20:04:33 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-28 20:04:33 | Glencourse (Kelani Ganga) | 11.07 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-28 20:04:07 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:03:53 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-28 20:03:50 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.040 |  |
| 2026-11-28 20:03:08 | Thanamalwila (Kirindi Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-11-28 20:02:56 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-28 20:02:36 | Dunamale (Aththanagalu Oya) | 3.86 | 🟡 Alert | -0.020 |  |
| 2026-11-28 20:02:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.096 |  |
| 2026-11-28 20:02:29 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.071 |  |
| 2026-11-28 20:02:18 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:02:13 | Kuda Oya (Kirindi Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-11-28 20:02:07 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | -0.063 |  |
| 2026-11-28 20:01:46 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-28 20:01:45 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:01:36 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-28 20:01:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:01:26 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-11-28 20:01:06 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:00:58 | Moraketiya (Walawe Ganga) | 3.05 | 🟡 Alert | 0.000 |  |
| 2026-11-28 20:00:48 | Moragaswewa (Deduru Oya) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-11-28 20:00:16 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 20:06:00 | Panadugama (Nilwala Ganga) | 5.17 | 🟡 Alert | 0.088 | 🔺 Rising |
| 2026-11-28 20:00:58 | Moraketiya (Walawe Ganga) | 3.05 | 🟡 Alert | 0.000 |  |
| 2026-11-28 20:07:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.000 |  |
| 2026-11-28 20:02:36 | Dunamale (Aththanagalu Oya) | 3.86 | 🟡 Alert | -0.020 |  |
| 2026-11-28 20:12:15 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-28 20:17:49 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-11-28 20:04:33 | Glencourse (Kelani Ganga) | 11.07 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-28 20:02:56 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-28 20:15:36 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-28 20:03:53 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-28 20:01:36 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-28 20:07:05 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-28 20:04:33 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-28 20:04:52 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-28 20:09:49 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 18:01:41 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 20:13:21 | Thalgahagoda (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 20:01:06 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:06:35 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:01:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:24:29 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:04:07 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:02:18 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:01:45 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-28 20:02:13 | Kuda Oya (Kirindi Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-11-28 20:03:08 | Thanamalwila (Kirindi Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-11-28 20:01:46 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-28 20:00:16 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-11-28 20:01:26 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-11-28 20:00:48 | Moragaswewa (Deduru Oya) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-11-28 18:03:25 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-11-28 18:03:29 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.030 |  |
| 2026-11-28 20:10:00 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-11-28 20:03:50 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.040 |  |
| 2026-11-28 20:04:44 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.040 |  |
| 2026-11-28 20:02:07 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | -0.063 |  |
| 2026-11-28 20:06:39 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.069 |  |
| 2026-11-28 20:02:29 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.071 |  |
| 2026-11-28 20:02:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)