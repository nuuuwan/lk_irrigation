# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_02:13:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,619 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 02:13:49 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.008 |  |
| 2026-05-27 02:10:41 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.029 |  |
| 2026-05-27 02:10:14 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.005 |  |
| 2026-05-27 02:09:34 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.058 |  |
| 2026-05-27 02:09:19 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:08:31 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | -0.048 |  |
| 2026-05-27 02:06:39 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-05-27 02:06:37 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-05-27 02:06:10 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.212 |  |
| 2026-05-27 02:05:30 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.037 |  |
| 2026-05-27 02:04:27 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.041 |  |
| 2026-05-27 02:03:59 | Hanwella (Kelani Ganga) | 4.36 | 🟢 Normal | -0.040 |  |
| 2026-05-27 02:03:57 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:03:52 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-05-27 02:03:39 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:03:28 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:03:13 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.277 |  |
| 2026-05-27 02:03:11 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:02:24 | Dunamale (Aththanagalu Oya) | 2.33 | 🟢 Normal | -0.050 |  |
| 2026-05-27 02:02:09 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:02:04 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:02:03 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:01:58 | Ellagawa (Kalu Ganga) | 8.66 | 🟢 Normal | -0.010 |  |
| 2026-05-27 02:01:56 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:01:48 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:37:11 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.005 |  |
| 2026-05-27 01:30:11 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 22:00:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-27 00:09:21 | Magura (Kalu Ganga) | 3.00 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-27 01:06:01 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-26 18:04:02 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 01:06:33 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:09:19 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:03:39 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:02:04 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:01:48 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:03:28 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:01:56 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:02:03 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:03:57 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:03:11 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:51 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:09:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:04:27 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-27 02:02:09 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:37:11 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.005 |  |
| 2026-05-27 02:10:14 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.005 |  |
| 2026-05-27 02:13:49 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.008 |  |
| 2026-05-27 02:06:39 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-05-27 02:03:52 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-05-27 01:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-05-27 02:06:37 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-05-27 02:01:58 | Ellagawa (Kalu Ganga) | 8.66 | 🟢 Normal | -0.010 |  |
| 2026-05-27 01:03:36 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-05-26 18:04:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-27 02:10:41 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.029 |  |
| 2026-05-27 01:10:55 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | -0.032 |  |
| 2026-05-27 02:05:30 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.037 |  |
| 2026-05-27 02:03:59 | Hanwella (Kelani Ganga) | 4.36 | 🟢 Normal | -0.040 |  |
| 2026-05-27 02:04:27 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.041 |  |
| 2026-05-27 02:08:31 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | -0.048 |  |
| 2026-05-27 02:02:24 | Dunamale (Aththanagalu Oya) | 2.33 | 🟢 Normal | -0.050 |  |
| 2026-05-27 01:03:57 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.054 |  |
| 2026-05-27 02:09:34 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.058 |  |
| 2026-05-27 02:06:10 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.212 |  |
| 2026-05-27 02:03:13 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.277 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)