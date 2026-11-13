# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_08:03:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,511 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 08:03:29 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 08:03:23 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | -0.062 |  |
| 2026-11-13 08:03:19 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | -0.079 |  |
| 2026-11-13 08:03:14 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-11-13 08:03:14 | Thaldena (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.043 |  |
| 2026-11-13 08:03:09 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | -0.194 |  |
| 2026-11-13 08:03:01 | Kuda Oya (Kirindi Oya) | 2.43 | 🟢 Normal | -0.097 |  |
| 2026-11-13 08:02:38 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-11-13 08:02:28 | Ellagawa (Kalu Ganga) | 8.04 | 🟢 Normal | -0.040 |  |
| 2026-11-13 08:02:23 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.090 |  |
| 2026-11-13 08:02:14 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:02:08 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-11-13 08:02:07 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-11-13 08:01:45 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -0.039 |  |
| 2026-11-13 08:01:13 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-11-13 08:00:57 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-11-13 08:00:22 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:00:12 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | -0.125 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 07:11:09 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 07:02:03 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 07:18:01 | Panadugama (Nilwala Ganga) | 6.34 | 🟠 Minor Flood | -0.017 |  |
| 2026-11-13 07:11:01 | Magura (Kalu Ganga) | 4.04 | 🟡 Alert | 0.000 |  |
| 2026-11-13 07:04:29 | Moraketiya (Walawe Ganga) | 3.14 | 🟡 Alert | 0.000 |  |
| 2026-11-13 07:05:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.000 |  |
| 2026-11-13 07:02:26 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | -0.030 |  |
| 2026-11-13 08:01:13 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-11-13 07:03:51 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-13 08:03:29 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 08:00:22 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-13 07:06:58 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:02:14 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-13 07:15:35 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-13 07:06:05 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-11-13 07:01:30 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | -0.001 |  |
| 2026-11-13 07:07:41 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.009 |  |
| 2026-11-13 08:00:57 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-11-13 08:03:14 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-11-13 07:08:04 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | -0.017 |  |
| 2026-11-13 07:14:44 | Urawa (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.017 |  |
| 2026-11-13 08:02:38 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-11-13 08:02:08 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-11-13 08:02:07 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-11-13 07:04:06 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-11-13 07:09:52 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.027 |  |
| 2026-11-13 07:01:08 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-11-13 07:09:09 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | -0.036 |  |
| 2026-11-13 08:01:45 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -0.039 |  |
| 2026-11-13 08:02:28 | Ellagawa (Kalu Ganga) | 8.04 | 🟢 Normal | -0.040 |  |
| 2026-11-13 08:03:14 | Thaldena (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.043 |  |
| 2026-11-13 08:03:23 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | -0.062 |  |
| 2026-11-13 08:03:19 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | -0.079 |  |
| 2026-11-13 07:01:18 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.081 |  |
| 2026-11-13 08:02:23 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.090 |  |
| 2026-11-13 08:03:01 | Kuda Oya (Kirindi Oya) | 2.43 | 🟢 Normal | -0.097 |  |
| 2026-11-13 08:00:12 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | -0.125 |  |
| 2026-11-13 08:03:09 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | -0.194 |  |
| 2026-11-13 07:05:16 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | -2.400 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)