# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_21:10:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,139 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 21:10:39 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.018 |  |
| 2026-05-29 21:08:57 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:08:07 | Putupaula (Kalu Ganga) | 2.69 | 🟢 Normal | -0.009 |  |
| 2026-05-29 21:07:59 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-29 21:07:58 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-29 21:06:02 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:05:33 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:05:16 | Ellagawa (Kalu Ganga) | 8.44 | 🟢 Normal | -0.022 |  |
| 2026-05-29 21:05:06 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-05-29 21:04:57 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | -0.011 |  |
| 2026-05-29 21:04:22 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 21:04:08 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:03:54 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:03:49 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-05-29 21:03:41 | Magura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.054 |  |
| 2026-05-29 21:03:26 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:03:24 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:03:23 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:03:23 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:03:14 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.058 |  |
| 2026-05-29 21:03:03 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.079 |  |
| 2026-05-29 21:02:41 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-29 21:02:31 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:02:30 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | -17.100 |  |
| 2026-05-29 21:02:30 | Rathnapura (Kalu Ganga) | 3.74 | 🟢 Normal | -0.065 |  |
| 2026-05-29 21:02:19 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:02:11 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.041 |  |
| 2026-05-29 21:01:54 | Baddegama (Gin Ganga) | 3.27 | 🟢 Normal | -0.021 |  |
| 2026-05-29 21:01:41 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:01:34 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-05-29 21:01:34 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:01:10 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -17.100 |  |
| 2026-05-29 21:01:10 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 20:10:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.72 | 🟠 Minor Flood | 0.028 | 🔺 Rising |
| 2026-05-29 21:04:22 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 21:03:23 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-29 20:04:36 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:03:24 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:03:14 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:01:41 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:02:19 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:04:21 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:03:54 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:04:08 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-29 20:04:44 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:08:57 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:03:26 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:01:10 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:02:31 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:05:33 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:06:02 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:01:34 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:01:26 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:03:23 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:08:07 | Putupaula (Kalu Ganga) | 2.69 | 🟢 Normal | -0.009 |  |
| 2026-05-29 21:07:58 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-29 21:02:41 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-29 21:07:59 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-29 21:04:57 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | -0.011 |  |
| 2026-05-29 21:10:39 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.018 |  |
| 2026-05-29 21:05:06 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-05-29 21:03:49 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-05-29 21:01:54 | Baddegama (Gin Ganga) | 3.27 | 🟢 Normal | -0.021 |  |
| 2026-05-29 21:05:16 | Ellagawa (Kalu Ganga) | 8.44 | 🟢 Normal | -0.022 |  |
| 2026-05-29 21:01:34 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-05-29 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.034 |  |
| 2026-05-29 21:02:11 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.041 |  |
| 2026-05-29 21:03:41 | Magura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.054 |  |
| 2026-05-29 21:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.058 |  |
| 2026-05-29 21:02:30 | Rathnapura (Kalu Ganga) | 3.74 | 🟢 Normal | -0.065 |  |
| 2026-05-29 21:03:03 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.079 |  |
| 2026-05-29 21:02:30 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | -17.100 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)