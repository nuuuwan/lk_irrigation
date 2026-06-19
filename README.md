# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_08:11:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,416 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 08:11:17 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.073 |  |
| 2026-06-19 08:08:28 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:08:15 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:08:10 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.088 |  |
| 2026-06-19 08:07:39 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-06-19 08:07:34 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-19 08:07:33 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.060 |  |
| 2026-06-19 08:07:13 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-19 08:05:48 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:05:46 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.021 |  |
| 2026-06-19 08:05:44 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.029 |  |
| 2026-06-19 08:05:18 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.040 |  |
| 2026-06-19 08:04:57 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:04:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:04:13 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-19 08:04:02 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:03:42 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:03:33 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:03:22 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-19 08:03:18 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-06-19 08:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:02:42 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.048 |  |
| 2026-06-19 08:02:36 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-19 08:02:33 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-19 08:02:33 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.041 |  |
| 2026-06-19 08:02:26 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:02:16 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:02:15 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:02:14 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:01:23 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:01:22 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.030 |  |
| 2026-06-19 08:00:45 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:00:32 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:00:27 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:00:24 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:00:09 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 07:38:34 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.073 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 08:02:36 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-19 08:07:13 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-19 08:07:34 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-19 08:03:22 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-19 08:02:33 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-19 08:04:13 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-19 08:00:09 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 08:00:32 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:00:24 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:02:14 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:04:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:00:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:04:02 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:06:17 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:02:26 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:08:28 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:04:57 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:02:15 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:02:16 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:08:15 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:05:48 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:03:33 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:00:45 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:03:42 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:01:23 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.010 |  |
| 2026-06-19 08:07:39 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-06-19 08:03:18 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-06-19 08:05:46 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.021 |  |
| 2026-06-19 07:19:24 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.024 |  |
| 2026-06-19 08:05:44 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.029 |  |
| 2026-06-19 08:01:22 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.030 |  |
| 2026-06-19 08:05:18 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.040 |  |
| 2026-06-19 08:02:33 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.041 |  |
| 2026-06-19 08:02:42 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.048 |  |
| 2026-06-19 08:07:33 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.060 |  |
| 2026-06-19 08:11:17 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.073 |  |
| 2026-06-19 08:08:10 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)