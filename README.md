# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_04:03:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,987 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 04:03:07 | Giriulla (Maha Oya) | 3.36 | 🟢 Normal | -0.169 |  |
| 2026-11-25 04:02:46 | Dunamale (Aththanagalu Oya) | 3.82 | 🟡 Alert | 0.000 |  |
| 2026-11-25 04:02:39 | Glencourse (Kelani Ganga) | 11.96 | 🟢 Normal | -0.191 |  |
| 2026-11-25 04:02:37 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.080 |  |
| 2026-11-25 04:02:20 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 04:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.043 |  |
| 2026-11-25 04:02:11 | Wellawaya (Kirindi Oya) | 2.01 | 🟢 Normal | 0.756 | 🔺 Rising |
| 2026-11-25 04:01:55 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | -0.040 |  |
| 2026-11-25 04:01:25 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 04:00:57 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-25 04:00:52 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-11-25 04:00:32 | Magura (Kalu Ganga) | 3.68 | 🟢 Normal | -0.080 |  |
| 2026-11-25 04:00:26 | Moraketiya (Walawe Ganga) | 3.50 | 🟡 Alert | -0.133 |  |
| 2026-11-25 03:39:01 | Urawa (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.016 |  |
| 2026-11-25 03:37:51 | Moraketiya (Walawe Ganga) | 3.55 | 🟡 Alert | -0.133 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 04:02:46 | Dunamale (Aththanagalu Oya) | 3.82 | 🟡 Alert | 0.000 |  |
| 2026-11-25 04:00:26 | Moraketiya (Walawe Ganga) | 3.50 | 🟡 Alert | -0.133 |  |
| 2026-11-25 03:10:52 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 135.000 | 🔺 Rising |
| 2026-11-25 04:02:11 | Wellawaya (Kirindi Oya) | 2.01 | 🟢 Normal | 0.756 | 🔺 Rising |
| 2026-11-25 03:05:48 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-11-25 03:05:01 | Rathnapura (Kalu Ganga) | 3.99 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-11-25 02:28:00 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-25 03:02:54 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-25 03:05:00 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-25 03:05:03 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-25 02:28:23 | Pitabeddara (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-25 04:00:57 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-25 03:09:46 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-25 03:02:44 | Kuda Oya (Kirindi Oya) | 2.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-25 02:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 03:15:04 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-25 03:06:02 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-25 00:44:51 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 03:02:37 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 03:01:05 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-25 04:02:20 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 04:01:25 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:02:13 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:01:28 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 04:00:52 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-11-25 03:39:01 | Urawa (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.016 |  |
| 2026-11-24 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.019 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 04:01:55 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | -0.040 |  |
| 2026-11-25 04:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.043 |  |
| 2026-11-25 03:07:40 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.071 |  |
| 2026-11-25 04:02:37 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.080 |  |
| 2026-11-25 04:00:32 | Magura (Kalu Ganga) | 3.68 | 🟢 Normal | -0.080 |  |
| 2026-11-25 03:01:33 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.082 |  |
| 2026-11-25 03:03:25 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.086 |  |
| 2026-11-25 03:00:26 | Siyambalanduwa (Heda Oya) | 2.55 | 🟢 Normal | -0.090 |  |
| 2026-11-25 04:03:07 | Giriulla (Maha Oya) | 3.36 | 🟢 Normal | -0.169 |  |
| 2026-11-25 04:02:39 | Glencourse (Kelani Ganga) | 11.96 | 🟢 Normal | -0.191 |  |
| 2026-11-25 03:18:03 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -2.667 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)