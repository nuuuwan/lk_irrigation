# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_18:30:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,793 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 18:30:09 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:13:17 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.034 |  |
| 2026-10-05 18:12:19 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:11:57 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-05 18:09:09 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-05 18:07:06 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:06:34 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-10-05 18:06:10 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-10-05 18:06:06 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-10-05 18:05:43 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:05:28 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:05:09 | Deraniyagala (Kelani Ganga) | 2.16 | 🟢 Normal | 1.157 | 🔺 Rising |
| 2026-10-05 18:05:03 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-05 18:04:58 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-05 18:04:47 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.049 |  |
| 2026-10-05 18:04:25 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-05 18:04:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:04:08 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:03:54 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-05 18:03:39 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-10-05 18:03:21 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:03:20 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.031 |  |
| 2026-10-05 18:03:17 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-10-05 18:03:15 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-10-05 18:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | -0.030 |  |
| 2026-10-05 18:03:04 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.131 |  |
| 2026-10-05 18:02:56 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-10-05 18:02:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-10-05 18:02:33 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.146 |  |
| 2026-10-05 18:02:12 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:01:59 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-05 18:01:51 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:01:48 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.081 |  |
| 2026-10-05 18:01:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:01:36 | Peradeniya (Mahaweli Ganga) | 3.19 | 🟢 Normal | 0.617 | 🔺 Rising |
| 2026-10-05 18:01:36 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.010 |  |
| 2026-10-05 18:01:07 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-05 18:00:41 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.032 |  |
| 2026-10-05 18:00:08 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 18:05:09 | Deraniyagala (Kelani Ganga) | 2.16 | 🟢 Normal | 1.157 | 🔺 Rising |
| 2026-10-05 18:01:36 | Peradeniya (Mahaweli Ganga) | 3.19 | 🟢 Normal | 0.617 | 🔺 Rising |
| 2026-10-05 18:03:17 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-10-05 18:06:10 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-10-05 18:01:59 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-05 18:03:54 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-05 18:04:25 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-05 18:04:58 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-05 18:09:09 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-05 18:05:03 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-05 18:11:57 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-05 18:01:36 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:05:28 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:01:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:05:43 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:04:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:30:09 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:01:51 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:00:08 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:02:12 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:03:21 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:07:06 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:02:56 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-10-05 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.010 |  |
| 2026-10-05 17:03:04 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-05 18:01:07 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-05 18:03:15 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-10-05 18:06:34 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-10-05 18:03:39 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-10-05 18:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | -0.030 |  |
| 2026-10-05 18:03:20 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.031 |  |
| 2026-10-05 18:02:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-10-05 18:00:41 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.032 |  |
| 2026-10-05 18:13:17 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.034 |  |
| 2026-10-05 18:06:06 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-10-05 18:04:47 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.049 |  |
| 2026-10-05 18:01:48 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.081 |  |
| 2026-10-05 18:03:04 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.131 |  |
| 2026-10-05 18:02:33 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)