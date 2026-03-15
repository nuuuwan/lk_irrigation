# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_22:16:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,381 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 22:16:11 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-15 22:11:38 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.064 |  |
| 2026-03-15 22:09:28 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.029 |  |
| 2026-03-15 22:07:29 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.018 |  |
| 2026-03-15 22:07:09 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-15 22:06:53 | Thaldena (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.139 |  |
| 2026-03-15 22:06:37 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:05:10 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:05:04 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.019 |  |
| 2026-03-15 22:05:03 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:05:03 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 22:05:01 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 22:04:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:04:27 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.040 |  |
| 2026-03-15 22:04:25 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:04:20 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-03-15 22:04:12 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-03-15 22:04:11 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 22:04:10 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-15 22:03:56 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.049 |  |
| 2026-03-15 22:03:55 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-03-15 22:03:35 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-03-15 22:03:09 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:02:57 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:02:36 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-15 22:02:15 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:02:15 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-15 22:02:06 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:01:49 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:01:42 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:01:24 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.011 |  |
| 2026-03-15 22:01:14 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:01:00 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:00:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.023 |  |
| 2026-03-15 22:00:54 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 22:02:36 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-15 22:05:03 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 22:07:09 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-15 22:02:15 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-15 22:04:11 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 22:05:01 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 22:16:11 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-15 22:01:00 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:01:42 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:02:57 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:01:14 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:05:04 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:00:54 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:01:49 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:03:09 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:05:10 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:06:37 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:04:25 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:05:03 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:02:20 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:04:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:02:06 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:02:15 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:03:55 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-03-15 22:04:10 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-15 22:04:20 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-03-15 22:01:24 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.011 |  |
| 2026-03-15 22:07:29 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.018 |  |
| 2026-03-15 21:10:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.019 |  |
| 2026-03-15 22:05:04 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.019 |  |
| 2026-03-15 22:03:35 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-03-15 22:04:12 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-03-15 22:00:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.023 |  |
| 2026-03-15 22:09:28 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.029 |  |
| 2026-03-15 22:04:27 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.040 |  |
| 2026-03-15 18:02:59 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.040 |  |
| 2026-03-15 22:03:56 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.049 |  |
| 2026-03-15 22:11:38 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.064 |  |
| 2026-03-15 22:06:53 | Thaldena (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)