# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_11:29:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,779 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 11:29:42 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.007 |  |
| 2026-04-05 11:24:20 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.008 |  |
| 2026-04-05 11:18:10 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:12:00 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.040 |  |
| 2026-04-05 11:08:06 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:07:24 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-04-05 11:07:20 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.052 |  |
| 2026-04-05 11:07:16 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:07:13 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:07:07 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:06:42 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:05:46 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-05 11:05:35 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.380 | 🔺 Rising |
| 2026-04-05 11:05:28 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-04-05 11:04:41 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-04-05 11:04:34 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:04:22 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:04:22 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-05 11:04:02 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.022 |  |
| 2026-04-05 11:03:57 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.059 |  |
| 2026-04-05 11:03:50 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-04-05 11:03:44 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.043 |  |
| 2026-04-05 11:03:36 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.089 |  |
| 2026-04-05 11:03:28 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 11:03:16 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-05 11:03:12 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-04-05 11:03:03 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.069 |  |
| 2026-04-05 11:02:57 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:02:41 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.011 |  |
| 2026-04-05 11:02:17 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:02:08 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.158 |  |
| 2026-04-05 11:02:08 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:01:24 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:01:11 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.065 |  |
| 2026-04-05 11:01:07 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:01:02 | Thanthirimale (Malwathu Oya) | 3.02 | 🟢 Normal | -0.041 |  |
| 2026-04-05 11:00:42 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:00:22 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 11:05:35 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.380 | 🔺 Rising |
| 2026-04-05 11:03:12 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-04-05 11:03:50 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-04-05 11:03:28 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 11:02:57 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:08:06 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:01:24 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:02:08 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:02:41 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:02:17 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:07:07 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:01:07 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:04:34 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:18:10 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:04:22 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:07:16 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:07:13 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:00:42 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-05 11:29:42 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.007 |  |
| 2026-04-05 11:24:20 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.008 |  |
| 2026-04-05 11:05:46 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-05 11:04:22 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-05 11:03:16 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-05 11:05:28 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-04-05 11:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.011 |  |
| 2026-04-05 11:04:02 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.022 |  |
| 2026-04-05 11:07:24 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-04-05 11:04:41 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-04-05 11:00:22 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | -0.032 |  |
| 2026-04-05 11:12:00 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.040 |  |
| 2026-04-05 11:01:02 | Thanthirimale (Malwathu Oya) | 3.02 | 🟢 Normal | -0.041 |  |
| 2026-04-05 11:03:44 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.043 |  |
| 2026-04-05 11:07:20 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.052 |  |
| 2026-04-05 11:03:57 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.059 |  |
| 2026-04-05 11:01:11 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.065 |  |
| 2026-04-05 11:03:03 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.069 |  |
| 2026-04-05 11:03:36 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.089 |  |
| 2026-04-05 11:02:08 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)