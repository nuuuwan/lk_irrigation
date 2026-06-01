# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_05:20:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,213 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 05:20:58 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.008 |  |
| 2026-06-01 05:18:03 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.078 |  |
| 2026-06-01 05:17:45 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.051 |  |
| 2026-06-01 05:15:27 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.018 |  |
| 2026-06-01 05:11:54 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.009 |  |
| 2026-06-01 05:10:27 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:09:04 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:07:20 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-01 05:06:59 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.010 |  |
| 2026-06-01 05:06:30 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:06:28 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-01 05:06:24 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-06-01 05:04:52 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:04:28 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-01 05:04:24 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:04:21 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:03:51 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | -0.123 |  |
| 2026-06-01 05:03:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:03:29 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:03:26 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.013 |  |
| 2026-06-01 05:03:19 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:03:14 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 13.714 | 🔺 Rising |
| 2026-06-01 05:03:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:02:53 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 13.714 | 🔺 Rising |
| 2026-06-01 05:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | -21.600 |  |
| 2026-06-01 05:02:30 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -21.600 |  |
| 2026-06-01 05:02:21 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-01 05:02:19 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:01:54 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.072 |  |
| 2026-06-01 05:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:01:08 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:00:58 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:00:56 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:00:49 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.030 |  |
| 2026-06-01 05:00:34 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:54:03 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.051 |  |
| 2026-06-01 04:50:49 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:50:28 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:48:19 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.051 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 05:03:14 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 13.714 | 🔺 Rising |
| 2026-06-01 05:07:20 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-01 05:04:28 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-01 05:06:28 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-01 05:02:30 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:03:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:03:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:00:58 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:02:55 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:00:34 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:01:08 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:06:10 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:10:27 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:04:21 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:09:04 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:02:19 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:06:30 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:04:52 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:00:56 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:04:24 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:03:29 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:03:19 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 05:20:58 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.008 |  |
| 2026-06-01 05:11:54 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.009 |  |
| 2026-06-01 05:06:59 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.010 |  |
| 2026-06-01 05:06:24 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-06-01 05:02:21 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-01 05:03:26 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.013 |  |
| 2026-06-01 05:15:27 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.018 |  |
| 2026-06-01 05:00:49 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.030 |  |
| 2026-06-01 05:17:45 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.051 |  |
| 2026-06-01 05:01:54 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.072 |  |
| 2026-06-01 05:18:03 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.078 |  |
| 2026-06-01 05:03:51 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | -0.123 |  |
| 2026-06-01 05:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | -21.600 |  |
| 2026-06-01 04:16:35 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -3618.000 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)