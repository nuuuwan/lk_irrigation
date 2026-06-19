# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_00:41:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,024 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 00:41:27 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | -0.028 |  |
| 2026-06-20 00:24:12 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.008 |  |
| 2026-06-20 00:13:45 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:12:23 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-06-20 00:11:10 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:09:18 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:07:17 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -54.000 |  |
| 2026-06-20 00:07:15 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -54.000 |  |
| 2026-06-20 00:07:06 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:06:24 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.205 |  |
| 2026-06-20 00:04:57 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-06-20 00:04:36 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:04:15 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-06-20 00:04:02 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:03:59 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:03:51 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-20 00:03:08 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:03:03 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:02:56 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:02:45 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:02:35 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:02:32 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.021 |  |
| 2026-06-20 00:02:27 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:02:17 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:02:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:01:49 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:01:43 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.030 |  |
| 2026-06-20 00:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-06-20 00:01:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:01:19 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:01:07 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-20 00:00:53 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.020 |  |
| 2026-06-19 23:57:25 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 22:06:17 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-06-20 00:03:51 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-19 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:02:27 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:01:19 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:03:03 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:01:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:09:18 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:00:11 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:00:15 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:02:45 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:02:56 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:03:59 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:11:10 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:01:49 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:02:35 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:02:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:07:06 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:04:02 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:13:45 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:02:17 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:03:08 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:04:36 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 00:24:12 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.008 |  |
| 2026-06-20 00:01:07 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:02:43 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 00:12:23 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-06-20 00:04:15 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-06-20 00:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-06-19 23:09:31 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.020 |  |
| 2026-06-20 00:04:57 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-06-20 00:00:53 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.020 |  |
| 2026-06-20 00:02:32 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.021 |  |
| 2026-06-20 00:41:27 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | -0.028 |  |
| 2026-06-20 00:01:43 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.030 |  |
| 2026-06-19 23:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | -0.033 |  |
| 2026-06-20 00:06:24 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.205 |  |
| 2026-06-20 00:07:17 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)