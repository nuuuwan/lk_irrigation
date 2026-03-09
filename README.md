# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_04:45:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **94,011 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 04:45:22 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:22:12 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-03-10 04:13:27 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:12:59 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:09:35 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-10 04:09:26 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.027 |  |
| 2026-03-10 04:07:59 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-10 04:06:57 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-10 04:05:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-03-10 04:05:05 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:04:19 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-10 04:04:07 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:04:01 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 04:03:33 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-10 04:03:21 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:02:31 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:02:19 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-03-10 04:02:18 | Dunamale (Aththanagalu Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:02:14 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:02:08 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:02:07 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:02:04 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-03-10 04:02:01 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.099 |  |
| 2026-03-10 04:02:00 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-10 04:01:49 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:01:47 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.216 |  |
| 2026-03-10 04:01:44 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:01:24 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:01:12 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:01:07 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.124 |  |
| 2026-03-10 04:00:57 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:00:39 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 04:22:12 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-03-10 04:05:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-03-09 18:01:06 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-10 02:08:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-03-10 04:02:00 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-09 22:02:21 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-10 04:06:57 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-10 04:04:19 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-10 04:09:35 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-10 04:04:01 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 04:02:04 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-03-10 04:00:57 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:02:08 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:02:07 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:02:14 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:45:22 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:01:24 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-09 18:06:39 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:11:47 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:05:04 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:03:21 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:00:22 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:01:12 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:01:44 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:02:18 | Dunamale (Aththanagalu Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:05:05 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:04:07 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:01:49 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:13:27 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:07:59 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-10 04:03:33 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-10 04:00:39 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-03-10 04:09:26 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.027 |  |
| 2026-03-10 04:02:19 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-03-09 18:01:53 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.075 |  |
| 2026-03-10 04:02:01 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.099 |  |
| 2026-03-10 04:01:07 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.124 |  |
| 2026-03-10 04:01:47 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.216 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)