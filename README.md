# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_04:27:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **232,907 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 04:27:47 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:13:27 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-08-14 04:11:23 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:10:59 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.021 |  |
| 2026-08-14 04:10:46 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-08-14 04:07:45 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-08-14 04:07:08 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:06:55 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-08-14 04:05:55 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.050 |  |
| 2026-08-14 04:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-14 04:05:09 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:04:46 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:04:24 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:04:23 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-14 04:03:53 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-08-14 04:03:01 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-14 04:02:57 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:02:39 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:02:28 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:02:23 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:02:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 04:01:50 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:01:42 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:00:44 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 03:44:32 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-14 04:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-14 03:08:09 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-14 04:04:23 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-14 04:00:44 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 04:02:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 04:02:57 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:02:28 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:07:08 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:04:46 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:01:42 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:13:34 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:02:23 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-08-14 02:00:08 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-14 03:09:00 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:27:47 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:05:09 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:02:39 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-14 03:06:04 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:04:24 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:11:23 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:06:46 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-14 03:03:23 | Peradeniya (Mahaweli Ganga) | 3.24 | 🟢 Normal | 0.000 |  |
| 2026-08-14 03:04:23 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-14 03:09:28 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:01:50 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-14 03:11:48 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-08-14 04:06:55 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-08-14 04:13:27 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-08-14 03:08:46 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-08-14 04:03:01 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-14 04:03:53 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-08-14 04:10:46 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-08-14 04:10:59 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.021 |  |
| 2026-08-14 04:07:45 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-08-14 03:04:44 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.029 |  |
| 2026-08-13 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.040 |  |
| 2026-08-14 04:05:55 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.050 |  |
| 2026-08-14 03:03:33 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | -0.174 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)