# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_23:03:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,650 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 23:03:21 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:03:07 | Norwood (Kelani Ganga) | 1.64 | 🟡 Alert | -0.080 |  |
| 2026-10-18 23:03:05 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-18 23:02:57 | Moragaswewa (Deduru Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-10-18 23:02:54 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-10-18 23:02:30 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.091 |  |
| 2026-10-18 23:02:17 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:02:14 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-18 23:02:09 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | -0.023 |  |
| 2026-10-18 23:02:03 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:01:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-10-18 23:01:39 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | -0.050 |  |
| 2026-10-18 23:01:33 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-10-18 23:01:23 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:01:16 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:00:42 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | -0.025 |  |
| 2026-10-18 22:39:15 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | 0.000 |  |
| 2026-10-18 22:27:25 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 22:01:59 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 22:39:15 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | 0.000 |  |
| 2026-10-18 23:03:07 | Norwood (Kelani Ganga) | 1.64 | 🟡 Alert | -0.080 |  |
| 2026-10-18 22:05:50 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.527 | 🔺 Rising |
| 2026-10-18 22:08:45 | Glencourse (Kelani Ganga) | 11.85 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-10-18 22:02:39 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-18 23:02:14 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-18 22:01:31 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 23:02:17 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:01:23 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-18 22:11:41 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:01:16 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-18 22:06:56 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:03:21 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 22:02:56 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:02:03 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-18 23:03:05 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-18 23:02:57 | Moragaswewa (Deduru Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-10-18 22:01:52 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-10-18 22:13:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.60 | 🟢 Normal | -0.017 |  |
| 2026-10-18 22:06:23 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-10-18 23:01:33 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-10-18 23:02:54 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-10-18 22:27:25 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | -0.022 |  |
| 2026-10-18 23:02:09 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | -0.023 |  |
| 2026-10-18 23:00:42 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | -0.025 |  |
| 2026-10-18 22:05:53 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | -0.029 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-18 23:01:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-10-18 21:03:08 | Urawa (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.043 |  |
| 2026-10-18 23:01:39 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | -0.050 |  |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |
| 2026-10-18 22:06:22 | Pitabeddara (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.052 |  |
| 2026-10-18 22:03:37 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.058 |  |
| 2026-10-18 22:07:16 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.059 |  |
| 2026-10-18 22:04:23 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | -0.066 |  |
| 2026-10-18 23:02:30 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.091 |  |
| 2026-10-18 22:09:59 | Rathnapura (Kalu Ganga) | 4.61 | 🟢 Normal | -1.208 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)