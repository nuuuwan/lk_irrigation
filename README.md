# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_11:17:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,462 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 11:17:58 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:17:06 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:14:37 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-04-17 11:12:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-04-17 11:09:43 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:07:18 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:06:15 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-17 11:06:04 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-04-17 11:05:53 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-17 11:05:53 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-04-17 11:05:10 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:04:29 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | -0.019 |  |
| 2026-04-17 11:04:27 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-04-17 11:04:07 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-04-17 11:04:05 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.031 |  |
| 2026-04-17 11:03:44 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:03:33 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-04-17 11:03:28 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.044 |  |
| 2026-04-17 11:03:27 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:03:24 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:03:10 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-17 11:03:00 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:02:58 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:02:52 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:02:44 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:02:24 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.303 | 🔺 Rising |
| 2026-04-17 11:02:22 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 11:02:15 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:02:14 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 11:02:09 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.060 |  |
| 2026-04-17 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-04-17 11:01:53 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:01:48 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:01:45 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:01:31 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:01:24 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:00:41 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 11:00:36 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:00:26 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:00:12 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 11:02:24 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.303 | 🔺 Rising |
| 2026-04-17 11:03:10 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-17 11:12:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-04-17 11:06:15 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-17 11:00:12 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-17 11:05:53 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-17 11:00:41 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 11:02:22 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 11:02:14 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 11:00:26 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:01:48 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:01:24 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:02:44 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:02:15 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:17:58 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:09:43 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:03:27 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:03:44 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:01:31 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:05:10 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:07:18 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:01:45 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:00:36 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:01:53 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:02:58 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:03:00 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:17:06 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-04-17 11:04:29 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | -0.019 |  |
| 2026-04-17 11:14:37 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-04-17 11:03:33 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-04-17 11:05:53 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-04-17 11:04:07 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-04-17 11:04:27 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-04-17 11:04:05 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.031 |  |
| 2026-04-17 11:06:04 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-04-17 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-04-17 11:03:28 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.044 |  |
| 2026-04-17 11:02:09 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)