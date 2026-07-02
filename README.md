# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_22:43:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **195,599 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 22:43:54 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:41:30 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:23:26 | Panadugama (Nilwala Ganga) | 0.57 | 🟢 Normal | -7.842 |  |
| 2026-07-02 22:16:11 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.024 |  |
| 2026-07-02 22:15:07 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-07-02 22:09:18 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:09:02 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:09:00 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:09:00 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:08:40 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -7.842 |  |
| 2026-07-02 22:08:04 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.056 |  |
| 2026-07-02 22:07:53 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:06:03 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.009 |  |
| 2026-07-02 22:05:34 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:05:01 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.060 |  |
| 2026-07-02 22:04:58 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-07-02 22:04:52 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:04:45 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-02 22:04:14 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:04:00 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:03:55 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-07-02 22:03:42 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.095 |  |
| 2026-07-02 22:03:14 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:03:06 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 22:03:05 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:03:04 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.050 |  |
| 2026-07-02 22:02:37 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:02:17 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:01:55 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.041 |  |
| 2026-07-02 22:01:31 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:01:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:01:11 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:01:10 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:00:36 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:00:26 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 22:04:58 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-07-02 22:03:06 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:43:54 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:01:11 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:09:00 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:01:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:01:10 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:00:36 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:58 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-02 21:20:24 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:09:02 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:41:30 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:01:31 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:02:37 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:04:00 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:03:05 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:09:18 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:04:52 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:05:34 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:02:17 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:04:14 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:51:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:09:00 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:03:14 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-02 22:07:53 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-02 21:09:34 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-07-02 22:06:03 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.009 |  |
| 2026-07-02 22:15:07 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-07-02 22:03:55 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-07-02 22:04:45 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-02 20:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-07-02 22:16:11 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.024 |  |
| 2026-07-02 22:01:55 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.041 |  |
| 2026-07-02 22:03:04 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.050 |  |
| 2026-07-02 22:08:04 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.056 |  |
| 2026-07-02 22:05:01 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.060 |  |
| 2026-07-02 22:03:42 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.095 |  |
| 2026-07-02 22:23:26 | Panadugama (Nilwala Ganga) | 0.57 | 🟢 Normal | -7.842 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)