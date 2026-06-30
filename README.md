# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_21:12:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,787 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 21:12:20 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.005 |  |
| 2026-06-30 21:11:06 | Ellagawa (Kalu Ganga) | 7.35 | 🟢 Normal | -0.103 |  |
| 2026-06-30 21:09:52 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:09:21 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.075 |  |
| 2026-06-30 21:07:06 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-30 21:06:43 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.012 |  |
| 2026-06-30 21:06:30 | Putupaula (Kalu Ganga) | 1.63 | 🟢 Normal | -0.029 |  |
| 2026-06-30 21:05:50 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-06-30 21:05:15 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-06-30 21:04:58 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.042 |  |
| 2026-06-30 21:04:56 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-06-30 21:04:43 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.013 |  |
| 2026-06-30 21:04:25 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:04:20 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-30 21:04:03 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:04:02 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:03:40 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:03:29 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:03:04 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 21:02:49 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:02:48 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.043 |  |
| 2026-06-30 21:02:47 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.064 |  |
| 2026-06-30 21:02:44 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.020 |  |
| 2026-06-30 21:02:35 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.242 |  |
| 2026-06-30 21:02:32 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:02:30 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.040 |  |
| 2026-06-30 21:02:19 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:02:12 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.040 |  |
| 2026-06-30 21:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-06-30 21:02:11 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:01:44 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:01:28 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:01:13 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-30 21:01:12 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 21:04:20 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-30 21:01:13 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-30 21:07:06 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-30 21:03:04 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 21:02:32 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:02:11 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:03:40 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:04:03 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:01:44 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:08:51 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:04:02 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:04:25 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:01:28 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:02:49 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:09:52 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:02:19 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:02:00 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:01:12 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:03:29 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:12:20 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.005 |  |
| 2026-06-30 21:04:56 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-06-30 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-30 21:05:15 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-06-30 21:06:43 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.012 |  |
| 2026-06-30 21:04:43 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.013 |  |
| 2026-06-30 21:05:50 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-06-30 21:02:44 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.020 |  |
| 2026-06-30 21:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-06-30 21:06:30 | Putupaula (Kalu Ganga) | 1.63 | 🟢 Normal | -0.029 |  |
| 2026-06-30 20:11:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.039 |  |
| 2026-06-30 21:02:12 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.040 |  |
| 2026-06-30 21:02:30 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.040 |  |
| 2026-06-30 21:04:58 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.042 |  |
| 2026-06-30 21:02:48 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.043 |  |
| 2026-06-30 21:02:47 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.064 |  |
| 2026-06-30 21:09:21 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.075 |  |
| 2026-06-30 21:11:06 | Ellagawa (Kalu Ganga) | 7.35 | 🟢 Normal | -0.103 |  |
| 2026-06-30 21:02:35 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.242 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)