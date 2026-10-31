# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_00:03:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,393 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 00:03:09 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.021 |  |
| 2026-11-01 00:03:06 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-01 00:02:59 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.005 |  |
| 2026-11-01 00:02:41 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-01 00:02:39 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-11-01 00:02:35 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-11-01 00:02:21 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:10 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:09 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:00 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:00:54 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-11-01 00:00:07 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-31 23:51:03 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 22:03:23 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | -0.039 |  |
| 2026-10-31 23:03:09 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-31 23:10:09 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-31 23:08:09 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-31 23:05:51 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-31 23:01:43 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-31 23:01:52 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:00 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:03:32 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:10 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-10-31 23:04:59 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:09 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.000 |  |
| 2026-10-31 23:01:59 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:00:07 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:21 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-10-31 23:01:38 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-31 23:07:07 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-31 23:02:33 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-10-31 23:04:53 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:59 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.005 |  |
| 2026-10-31 23:10:23 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | -0.009 |  |
| 2026-11-01 00:02:35 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-01 00:03:06 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-01 00:02:41 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-01 00:02:39 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-11-01 00:00:54 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-10-31 18:01:51 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-31 23:51:03 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.017 |  |
| 2026-10-31 18:04:44 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.020 |  |
| 2026-11-01 00:03:09 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.021 |  |
| 2026-10-31 23:05:54 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.029 |  |
| 2026-10-31 23:02:46 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.031 |  |
| 2026-10-31 23:05:37 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.050 |  |
| 2026-10-31 22:03:00 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | -0.051 |  |
| 2026-10-31 23:04:15 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.090 |  |
| 2026-10-31 23:01:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.08 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)