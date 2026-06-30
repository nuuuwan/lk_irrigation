# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_10:27:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,366 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 10:27:48 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:21:18 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.124 |  |
| 2026-06-30 10:18:21 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:13:13 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-06-30 10:11:44 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.009 |  |
| 2026-06-30 10:08:17 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:07:34 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.054 |  |
| 2026-06-30 10:05:53 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:05:48 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:05:36 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:05:29 | Ellagawa (Kalu Ganga) | 7.94 | 🟢 Normal | -0.024 |  |
| 2026-06-30 10:05:21 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.038 |  |
| 2026-06-30 10:04:36 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.129 |  |
| 2026-06-30 10:04:03 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:04:01 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.067 |  |
| 2026-06-30 10:03:52 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-30 10:03:50 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.081 |  |
| 2026-06-30 10:03:42 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:03:33 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | -0.085 |  |
| 2026-06-30 10:03:28 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:03:18 | Putupaula (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-06-30 10:03:16 | Kithulgala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-06-30 10:03:13 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-06-30 10:03:02 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-30 10:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | -0.059 |  |
| 2026-06-30 10:02:44 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:02:41 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-30 10:02:41 | Baddegama (Gin Ganga) | 2.79 | 🟢 Normal | -0.037 |  |
| 2026-06-30 10:02:39 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:02:30 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-06-30 10:02:30 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-06-30 10:02:12 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:02:06 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-06-30 10:01:19 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-06-30 10:01:17 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:01:07 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.042 |  |
| 2026-06-30 10:00:52 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:00:33 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:00:32 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 10:02:41 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-30 10:02:12 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:03:42 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:27:48 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:00:32 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:04:03 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:01:17 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:08:17 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:00:52 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:00:33 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:18:21 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:02:44 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:05:48 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:02:06 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:05:53 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:03:28 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:05:36 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-30 10:11:44 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.009 |  |
| 2026-06-30 10:13:13 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-06-30 10:03:02 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-30 10:02:30 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-06-30 10:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-06-30 10:03:18 | Putupaula (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-06-30 10:03:52 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-30 10:03:16 | Kithulgala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-06-30 10:03:13 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-06-30 10:01:19 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-06-30 10:02:30 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-06-30 10:05:29 | Ellagawa (Kalu Ganga) | 7.94 | 🟢 Normal | -0.024 |  |
| 2026-06-30 10:02:41 | Baddegama (Gin Ganga) | 2.79 | 🟢 Normal | -0.037 |  |
| 2026-06-30 10:05:21 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.038 |  |
| 2026-06-30 10:01:07 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.042 |  |
| 2026-06-30 10:07:34 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.054 |  |
| 2026-06-30 10:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | -0.059 |  |
| 2026-06-30 10:04:01 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.067 |  |
| 2026-06-30 10:03:50 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.081 |  |
| 2026-06-30 10:03:33 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | -0.085 |  |
| 2026-06-30 10:21:18 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.124 |  |
| 2026-06-30 10:04:36 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)