# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_00:03:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,534 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Magura — Alert; 🟡 Thawalama — Alert; 🟡 Rathnapura — Alert; 🟡 Peradeniya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 00:03:05 | Rathnapura (Kalu Ganga) | 5.43 | 🟡 Alert | 0.066 | 🔺 Rising |
| 2026-11-10 00:03:03 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.072 |  |
| 2026-11-10 00:02:42 | Peradeniya (Mahaweli Ganga) | 5.16 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-11-10 00:02:38 | Thawalama (Gin Ganga) | 4.65 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-11-10 00:02:17 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.050 |  |
| 2026-11-10 00:02:11 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | -0.011 |  |
| 2026-11-10 00:02:11 | Glencourse (Kelani Ganga) | 14.90 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-10 00:01:55 | Panadugama (Nilwala Ganga) | 5.30 | 🟡 Alert | 0.022 | 🔺 Rising |
| 2026-11-10 00:01:52 | Nawalapitiya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.073 |  |
| 2026-11-10 00:01:47 | Wellawaya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.092 |  |
| 2026-11-10 00:01:38 | Giriulla (Maha Oya) | 2.61 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-10 00:01:34 | Pitabeddara (Nilwala Ganga) | 3.05 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-11-10 00:00:27 | Moragaswewa (Deduru Oya) | 3.06 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-10 00:00:18 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-09 23:58:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.006 |  |
| 2026-11-09 23:36:29 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 23:04:01 | Dunamale (Aththanagalu Oya) | 4.44 | 🟠 Minor Flood | 0.039 | 🔺 Rising |
| 2026-11-09 23:03:27 | Moraketiya (Walawe Ganga) | 4.10 | 🟡 Alert | 0.772 | 🔺 Rising |
| 2026-11-09 23:06:17 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | 0.125 | 🔺 Rising |
| 2026-11-10 00:02:38 | Thawalama (Gin Ganga) | 4.65 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-11-10 00:03:05 | Rathnapura (Kalu Ganga) | 5.43 | 🟡 Alert | 0.066 | 🔺 Rising |
| 2026-11-10 00:02:42 | Peradeniya (Mahaweli Ganga) | 5.16 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-11-09 23:13:45 | Baddegama (Gin Ganga) | 3.80 | 🟡 Alert | 0.044 | 🔺 Rising |
| 2026-11-10 00:01:55 | Panadugama (Nilwala Ganga) | 5.30 | 🟡 Alert | 0.022 | 🔺 Rising |
| 2026-11-09 23:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.22 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-09 23:00:27 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | -0.022 |  |
| 2026-11-09 23:04:05 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | 0.436 | 🔺 Rising |
| 2026-11-09 23:04:22 | Thanamalwila (Kirindi Oya) | 3.02 | 🟢 Normal | 0.407 | 🔺 Rising |
| 2026-11-10 00:01:34 | Pitabeddara (Nilwala Ganga) | 3.05 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-11-09 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-09 23:03:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-10 00:02:11 | Glencourse (Kelani Ganga) | 14.90 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-09 23:02:16 | Ellagawa (Kalu Ganga) | 8.38 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-10 00:00:27 | Moragaswewa (Deduru Oya) | 3.06 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-10 00:01:38 | Giriulla (Maha Oya) | 2.61 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-09 23:02:49 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-09 18:06:18 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 00:00:18 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-09 23:36:29 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-09 23:07:22 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-09 23:58:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.006 |  |
| 2026-11-09 18:01:00 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-10 00:02:11 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | -0.011 |  |
| 2026-11-09 23:18:25 | Putupaula (Kalu Ganga) | 2.25 | 🟢 Normal | -0.018 |  |
| 2026-11-09 23:03:16 | Kuda Oya (Kirindi Oya) | 2.96 | 🟢 Normal | -0.020 |  |
| 2026-11-10 00:02:17 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.050 |  |
| 2026-11-10 00:03:03 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.072 |  |
| 2026-11-10 00:01:52 | Nawalapitiya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.073 |  |
| 2026-11-09 23:01:47 | Nakkala (Kumbukkan Oya) | 1.82 | 🟢 Normal | -0.079 |  |
| 2026-11-10 00:01:47 | Wellawaya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.092 |  |
| 2026-11-09 23:06:33 | Holombuwa (Kelani Ganga) | 1.75 | 🟢 Normal | -0.094 |  |
| 2026-11-09 23:03:43 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | -0.154 |  |
| 2026-11-09 23:06:57 | Thaldena (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.158 |  |
| 2026-11-09 23:03:36 | Deraniyagala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.293 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)