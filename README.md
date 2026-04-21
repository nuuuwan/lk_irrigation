# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_09:25:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,931 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 09:25:40 | Galgamuwa (Mee Oya) | 1.14 | 🟢 Normal | -0.007 |  |
| 2026-04-21 09:13:33 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.151 |  |
| 2026-04-21 09:13:15 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.020 |  |
| 2026-04-21 09:10:15 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.041 |  |
| 2026-04-21 09:09:16 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-04-21 09:09:07 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-21 09:06:25 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.029 |  |
| 2026-04-21 09:06:16 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-04-21 09:06:15 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 09:06:00 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.060 |  |
| 2026-04-21 09:05:40 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 09:05:33 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 09:05:00 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-21 09:04:53 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.098 |  |
| 2026-04-21 09:04:23 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.021 |  |
| 2026-04-21 09:03:42 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | -0.042 |  |
| 2026-04-21 09:03:36 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-04-21 09:03:29 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-21 09:03:27 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 09:03:26 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-21 09:03:26 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-21 09:03:20 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | -0.109 |  |
| 2026-04-21 09:03:04 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-04-21 09:02:25 | Thanamalwila (Kirindi Oya) | 1.98 | 🟢 Normal | -0.220 |  |
| 2026-04-21 09:02:21 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-04-21 09:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-21 09:01:59 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.050 |  |
| 2026-04-21 09:01:46 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 09:01:43 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 09:01:42 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-21 09:01:37 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.043 |  |
| 2026-04-21 09:01:30 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.023 |  |
| 2026-04-21 09:01:24 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-04-21 09:01:09 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-04-21 09:00:56 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.355 |  |
| 2026-04-21 09:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-04-21 09:00:37 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-21 09:00:18 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.040 |  |
| 2026-04-21 09:00:09 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 09:06:16 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-04-21 09:03:26 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-21 09:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-21 09:03:26 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-21 09:01:46 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 09:05:00 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-21 09:01:43 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 09:05:40 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 09:01:42 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-21 09:06:15 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 09:03:27 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 09:05:33 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 09:09:07 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-21 09:25:40 | Galgamuwa (Mee Oya) | 1.14 | 🟢 Normal | -0.007 |  |
| 2026-04-21 09:03:29 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-21 09:00:37 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-21 09:02:21 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-04-21 09:09:16 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-04-21 09:13:15 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.020 |  |
| 2026-04-21 09:03:04 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-04-21 09:03:36 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-04-21 09:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-04-21 09:04:23 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.021 |  |
| 2026-04-21 09:01:09 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-04-21 09:01:24 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-04-21 09:01:30 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.023 |  |
| 2026-04-21 09:06:25 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.029 |  |
| 2026-04-21 09:00:09 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.040 |  |
| 2026-04-21 09:00:18 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.040 |  |
| 2026-04-21 09:10:15 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.041 |  |
| 2026-04-21 09:03:42 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | -0.042 |  |
| 2026-04-21 09:01:37 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.043 |  |
| 2026-04-21 09:01:59 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.050 |  |
| 2026-04-21 09:06:00 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.060 |  |
| 2026-04-21 09:04:53 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.098 |  |
| 2026-04-21 09:03:20 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | -0.109 |  |
| 2026-04-21 09:13:33 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.151 |  |
| 2026-04-21 09:02:25 | Thanamalwila (Kirindi Oya) | 1.98 | 🟢 Normal | -0.220 |  |
| 2026-04-21 09:00:56 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.355 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)