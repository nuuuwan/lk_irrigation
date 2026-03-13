# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_13:18:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,260 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 13:18:32 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:13:34 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-03-13 13:13:02 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-03-13 13:12:56 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-13 13:11:31 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:09:15 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-13 13:08:58 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 13:08:08 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:07:49 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-13 13:07:36 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-03-13 13:07:28 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:06:46 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:06:28 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:06:04 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:05:40 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:05:24 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:05:08 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-03-13 13:04:51 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.134 |  |
| 2026-03-13 13:04:22 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:04:08 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:03:59 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:03:28 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-03-13 13:03:18 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.071 |  |
| 2026-03-13 13:02:54 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.060 |  |
| 2026-03-13 13:02:51 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.056 |  |
| 2026-03-13 13:02:32 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.099 |  |
| 2026-03-13 13:02:16 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-03-13 13:02:07 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:01:59 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:01:28 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:01:14 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:01:05 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-03-13 13:00:54 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-13 13:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-13 13:00:23 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:00:21 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:00:09 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:00:07 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.270 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 13:13:02 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-03-13 13:09:15 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-13 13:12:56 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-13 13:00:54 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-13 13:13:34 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-03-13 13:08:58 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 13:05:24 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:02:07 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:01:14 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:01:59 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:11:31 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:01:28 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 12:03:19 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:18:32 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:00:23 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:05:40 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:00:09 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:07:28 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:04:22 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:04:08 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:06:28 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:06:04 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:02:16 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:03:59 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:08:08 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:06:46 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 13:05:08 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-03-13 13:07:49 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-13 13:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-13 13:03:28 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-03-13 13:07:36 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-03-13 13:01:05 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-03-13 13:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-03-13 13:02:51 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.056 |  |
| 2026-03-13 13:02:54 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.060 |  |
| 2026-03-13 13:03:18 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.071 |  |
| 2026-03-13 13:02:32 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.099 |  |
| 2026-03-13 13:04:51 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.134 |  |
| 2026-03-13 13:00:07 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.270 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)