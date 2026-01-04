# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_22:07:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,767 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 22:07:43 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:07:22 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:05:49 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:05:16 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:05:14 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:04:39 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-01-04 22:04:04 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:03:43 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-04 22:03:41 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.059 |  |
| 2026-01-04 22:03:02 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-01-04 22:02:57 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:02:54 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-04 22:02:51 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-04 22:02:49 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:02:48 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.033 |  |
| 2026-01-04 22:02:28 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:02:24 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:02:00 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.041 |  |
| 2026-01-04 22:01:40 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-04 22:01:38 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:01:34 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:01:17 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-01-04 22:01:17 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.031 |  |
| 2026-01-04 22:01:11 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.021 |  |
| 2026-01-04 22:01:09 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:01:06 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:00:52 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-01-04 21:18:52 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:10:45 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 22:02:54 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-04 18:04:42 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-04 21:05:53 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-04 22:02:24 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:01:34 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:02:49 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:04:04 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:05:49 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:02:28 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:01:38 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:01:06 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:02:57 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:05:16 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:07:22 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:05:14 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:32 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:18:52 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:01:09 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:07:43 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-04 22:02:51 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-04 22:01:40 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-04 22:01:17 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-01-04 21:02:08 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-01-04 22:03:43 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-04 21:10:45 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-01-04 22:03:02 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-01-04 22:00:52 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-01-04 21:02:04 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-01-04 22:01:11 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.021 |  |
| 2026-01-04 21:08:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-01-04 21:02:53 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.022 |  |
| 2026-01-04 22:04:39 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-01-04 22:01:17 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.031 |  |
| 2026-01-04 22:02:48 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.033 |  |
| 2026-01-04 22:02:00 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.041 |  |
| 2026-01-04 18:15:36 | Galgamuwa (Mee Oya) | 2.40 | 🟢 Normal | -0.048 |  |
| 2026-01-04 21:08:54 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.050 |  |
| 2026-01-04 22:03:41 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)