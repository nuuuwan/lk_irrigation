# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_02:00:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,251 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 02:00:49 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.005 |  |
| 2026-06-09 02:00:08 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:43:27 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-06-09 01:28:45 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:22:26 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.027 |  |
| 2026-06-09 01:19:25 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:15:14 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-06-09 01:11:32 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 01:15:14 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-06-09 01:03:25 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-08 18:00:59 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-09 00:02:07 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-09 01:03:19 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-09 01:43:27 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-06-09 01:06:05 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:00:08 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:03:48 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:03:06 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:03:33 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:28:45 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 18:07:32 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:05:27 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:06:01 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:06:16 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:11:32 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:19:25 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-09 00:03:46 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:04:34 | Dunamale (Aththanagalu Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-06-09 00:03:38 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:01:58 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-09 00:01:10 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:00:49 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.005 |  |
| 2026-06-08 22:08:43 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-06-09 01:06:33 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-06-08 23:14:23 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.019 |  |
| 2026-06-09 01:03:14 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.020 |  |
| 2026-06-09 01:04:32 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-06-09 01:22:26 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.027 |  |
| 2026-06-09 01:06:29 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.028 |  |
| 2026-06-09 01:04:42 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.028 |  |
| 2026-06-09 00:00:13 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-06-09 00:02:41 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.033 |  |
| 2026-06-08 18:02:35 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.040 |  |
| 2026-06-09 01:02:08 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | -0.045 |  |
| 2026-06-09 00:10:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.057 |  |
| 2026-06-09 00:06:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | -0.084 |  |
| 2026-06-09 01:05:41 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)