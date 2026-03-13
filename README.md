# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_14:26:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,299 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 14:26:59 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 14:15:22 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 14:11:31 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:10:09 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:08:44 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:08:24 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-03-13 14:08:24 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.018 |  |
| 2026-03-13 14:08:12 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:08:06 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:07:52 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-03-13 14:07:16 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:07:12 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-03-13 14:07:06 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-03-13 14:06:28 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:06:05 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.025 |  |
| 2026-03-13 14:05:14 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.009 |  |
| 2026-03-13 14:05:02 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.058 |  |
| 2026-03-13 14:04:59 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-03-13 14:04:33 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:04:24 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-03-13 14:03:44 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.022 |  |
| 2026-03-13 14:03:37 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-03-13 14:03:31 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-03-13 14:03:14 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 14:03:09 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-13 14:03:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-13 14:02:52 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-03-13 14:02:49 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-13 14:02:48 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:02:41 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-03-13 14:02:20 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-03-13 14:02:01 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:01:58 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:01:49 | Weraganthota (Mahaweli Ganga) | -2.59 | 🟢 Normal | -0.088 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 14:07:52 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-03-13 14:04:24 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-03-13 14:08:24 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-03-13 14:03:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-13 14:03:09 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-13 14:26:59 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 14:03:14 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 14:15:22 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 14:08:12 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:02:01 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:01:09 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:01:58 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:10:09 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:11:31 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:04:33 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:01:16 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:08:44 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:02:48 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:06:28 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:08:06 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:02:20 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:07:16 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:05:14 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.009 |  |
| 2026-03-13 14:03:31 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-03-13 14:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-13 14:02:49 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-13 14:02:52 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-03-13 14:00:46 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-03-13 14:08:24 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.018 |  |
| 2026-03-13 14:07:12 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-03-13 14:04:59 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-03-13 14:03:44 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.022 |  |
| 2026-03-13 14:06:05 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.025 |  |
| 2026-03-13 14:07:06 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-03-13 14:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-03-13 14:02:41 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-03-13 14:03:37 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-03-13 14:05:02 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.058 |  |
| 2026-03-13 14:01:49 | Weraganthota (Mahaweli Ganga) | -2.59 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)