# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_23:20:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,510 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 23:20:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:08:56 | Rathnapura (Kalu Ganga) | 3.31 | 🟢 Normal | 0.456 | 🔺 Rising |
| 2026-06-05 23:07:15 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.013 |  |
| 2026-06-05 23:07:11 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-06-05 23:07:02 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-06-05 23:06:53 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-06-05 23:06:20 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:05:44 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.048 |  |
| 2026-06-05 23:05:42 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-06-05 23:05:39 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:04:47 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.012 |  |
| 2026-06-05 23:04:06 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 23:04:05 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 23:03:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:03:22 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 23:03:17 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:03:01 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:03:00 | Deraniyagala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-06-05 23:02:47 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-05 23:02:45 | Dunamale (Aththanagalu Oya) | 3.08 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-05 23:02:29 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.125 |  |
| 2026-06-05 23:02:26 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-05 23:02:25 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:02:13 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:01:57 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.034 |  |
| 2026-06-05 23:01:23 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:01:19 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-05 23:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-05 23:01:18 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-06-05 23:01:09 | Ellagawa (Kalu Ganga) | 7.12 | 🟢 Normal | -0.010 |  |
| 2026-06-05 23:00:55 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 23:08:56 | Rathnapura (Kalu Ganga) | 3.31 | 🟢 Normal | 0.456 | 🔺 Rising |
| 2026-06-05 23:05:42 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-06-05 23:03:00 | Deraniyagala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-06-05 23:02:45 | Dunamale (Aththanagalu Oya) | 3.08 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-05 23:02:47 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-05 23:02:26 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-05 23:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-05 21:16:46 | Putupaula (Kalu Ganga) | 1.61 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-05 23:03:22 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 23:04:06 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 23:04:05 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 18:01:21 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 23:05:39 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:01:23 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-05 21:01:23 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:02:25 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:00:55 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:06:46 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:03:01 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-05 22:02:43 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:03:17 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:02:13 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-05 22:28:18 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:03:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:06:20 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:20:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:01:18 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-06-05 23:07:02 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-06-05 23:01:19 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-05 23:01:09 | Ellagawa (Kalu Ganga) | 7.12 | 🟢 Normal | -0.010 |  |
| 2026-06-05 23:06:53 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-06-05 23:04:47 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.012 |  |
| 2026-06-05 23:07:15 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.013 |  |
| 2026-06-05 23:07:11 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-06-05 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-05 22:05:23 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.028 |  |
| 2026-06-05 23:01:57 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.034 |  |
| 2026-06-05 23:05:44 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.048 |  |
| 2026-06-05 23:02:29 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)