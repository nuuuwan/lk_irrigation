# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_09:14:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,136 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 09:14:09 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:10:17 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:09:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.064 |  |
| 2026-04-10 09:09:01 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:08:35 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.034 |  |
| 2026-04-10 09:07:02 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:06:55 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.022 |  |
| 2026-04-10 09:06:13 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.011 |  |
| 2026-04-10 09:05:38 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-04-10 09:05:22 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:05:15 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.070 |  |
| 2026-04-10 09:05:05 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:04:50 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:04:47 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-10 09:04:20 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-10 09:04:17 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-10 09:04:02 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:03:58 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 09:03:53 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:03:35 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-04-10 09:03:34 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:03:29 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:03:09 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:02:41 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-10 09:02:10 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.181 |  |
| 2026-04-10 09:01:58 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.110 |  |
| 2026-04-10 09:01:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:01:25 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:01:18 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-10 09:01:14 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:01:11 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:00:40 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:00:36 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-10 09:00:36 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.038 |  |
| 2026-04-10 09:00:35 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:00:30 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-04-10 09:00:13 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 08:45:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.181 |  |
| 2026-04-10 08:44:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.181 |  |
| 2026-04-10 08:44:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.181 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 09:04:17 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-10 09:00:36 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-10 09:02:41 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-10 09:03:58 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 09:00:35 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:03:29 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:01:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:03:53 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:14:09 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:04:50 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:03:09 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:01:11 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:09:01 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:10:17 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:04:02 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:01:25 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:00:13 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:03:34 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:02:10 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:05:05 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:00:40 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:07:02 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:01:14 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:05:22 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:04:47 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-10 09:04:20 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-10 09:00:30 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-04-10 09:06:13 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.011 |  |
| 2026-04-10 09:05:38 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-04-10 09:01:18 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-10 09:06:55 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.022 |  |
| 2026-04-10 09:03:35 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-04-10 09:08:35 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.034 |  |
| 2026-04-10 09:00:36 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.038 |  |
| 2026-04-10 08:03:58 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.050 |  |
| 2026-04-10 09:09:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.064 |  |
| 2026-04-10 09:05:15 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.070 |  |
| 2026-04-10 09:01:58 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.110 |  |
| 2026-04-10 09:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)