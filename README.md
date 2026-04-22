# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_12:20:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,947 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 12:20:23 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:13:24 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:08:37 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-22 12:07:00 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.018 |  |
| 2026-04-22 12:06:59 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-04-22 12:06:42 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-04-22 12:06:38 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:06:38 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-22 12:06:38 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:06:20 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.075 |  |
| 2026-04-22 12:04:50 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:04:42 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:04:19 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.020 |  |
| 2026-04-22 12:04:11 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 12:03:56 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:03:42 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.078 |  |
| 2026-04-22 12:03:41 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:03:30 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:03:05 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-04-22 12:03:01 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.020 |  |
| 2026-04-22 12:02:56 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:02:42 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 12:02:33 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.091 |  |
| 2026-04-22 12:02:33 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:02:25 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.035 |  |
| 2026-04-22 12:02:23 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | -0.044 |  |
| 2026-04-22 12:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 12:02:20 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.041 |  |
| 2026-04-22 12:02:14 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-04-22 12:02:10 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:02:06 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 12:01:48 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.063 |  |
| 2026-04-22 12:01:44 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-22 12:01:44 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:01:44 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:01:06 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-04-22 12:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-04-22 12:00:18 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 12:01:44 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-22 12:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 12:04:11 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 12:02:06 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 12:01:44 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:03:41 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:04:42 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 11:01:10 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:06:38 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:04:50 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:01:44 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:06:38 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:20:23 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:03:30 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:13:24 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:03:56 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:02:33 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:02:56 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:06:59 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-04-22 12:08:37 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-22 12:02:42 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 12:06:38 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-22 12:06:42 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-04-22 12:02:14 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-04-22 12:07:00 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.018 |  |
| 2026-04-22 11:03:19 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-04-22 12:04:19 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.020 |  |
| 2026-04-22 12:01:06 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-04-22 12:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-04-22 12:03:01 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.020 |  |
| 2026-04-22 12:00:18 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-04-22 12:02:25 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.035 |  |
| 2026-04-22 12:03:05 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-04-22 12:02:20 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.041 |  |
| 2026-04-22 12:02:23 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | -0.044 |  |
| 2026-04-22 12:01:48 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.063 |  |
| 2026-04-22 12:06:20 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.075 |  |
| 2026-04-22 12:03:42 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.078 |  |
| 2026-04-22 12:02:33 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)