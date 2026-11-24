# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_02:28:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,936 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 02:28:38 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.042 |  |
| 2026-11-25 02:28:23 | Pitabeddara (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-25 02:28:00 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-25 02:24:33 | Urawa (Nilwala Ganga) | 1.51 | 🟢 Normal | -11.077 |  |
| 2026-11-25 02:24:07 | Urawa (Nilwala Ganga) | 1.59 | 🟢 Normal | -11.077 |  |
| 2026-11-25 02:22:10 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-25 02:17:28 | Rathnapura (Kalu Ganga) | 3.89 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-25 02:16:44 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-11-25 02:13:51 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 02:10:31 | Moraketiya (Walawe Ganga) | 3.52 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-25 02:10:20 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-25 02:06:56 | Siyambalanduwa (Heda Oya) | 2.63 | 🟢 Normal | -0.182 |  |
| 2026-11-25 02:06:33 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-11-25 02:05:52 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-25 02:04:57 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-25 02:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 02:04:24 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 02:03:57 | Dunamale (Aththanagalu Oya) | 3.82 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-25 02:10:31 | Moraketiya (Walawe Ganga) | 3.52 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-25 02:02:22 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-11-25 02:17:28 | Rathnapura (Kalu Ganga) | 3.89 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-25 01:20:13 | Badalgama (Maha Oya) | 3.82 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-11-25 02:10:20 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-25 02:28:00 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-25 02:04:57 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-25 02:02:09 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-25 02:28:23 | Pitabeddara (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-25 02:02:17 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-25 02:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 02:13:51 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 02:22:10 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-25 00:44:51 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 02:01:34 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 02:01:21 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 02:03:04 | Giriulla (Maha Oya) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:02:13 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-25 01:05:08 | Thaldena (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-25 02:16:44 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-11-25 02:04:24 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:01:28 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 01:59:24 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-25 01:05:03 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-24 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.019 |  |
| 2026-11-25 02:05:52 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 02:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-11-25 02:28:38 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.042 |  |
| 2026-11-25 01:03:30 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.050 |  |
| 2026-11-25 02:00:15 | Magura (Kalu Ganga) | 3.85 | 🟢 Normal | -0.116 |  |
| 2026-11-25 02:03:19 | Peradeniya (Mahaweli Ganga) | 3.92 | 🟢 Normal | -0.135 |  |
| 2026-11-25 02:04:19 | Glencourse (Kelani Ganga) | 12.31 | 🟢 Normal | -0.158 |  |
| 2026-11-25 02:06:56 | Siyambalanduwa (Heda Oya) | 2.63 | 🟢 Normal | -0.182 |  |
| 2026-11-25 02:02:36 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.248 |  |
| 2026-11-25 01:09:13 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.263 |  |
| 2026-11-24 22:30:21 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -1.256 |  |
| 2026-11-25 02:24:33 | Urawa (Nilwala Ganga) | 1.51 | 🟢 Normal | -11.077 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)