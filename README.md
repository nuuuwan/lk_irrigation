# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_00:15:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **195,660 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 00:15:10 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-07-03 00:12:53 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-07-03 00:10:21 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:06:35 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-07-03 00:06:22 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:06:18 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:05:58 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-07-03 00:05:55 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:05:52 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-07-03 00:05:21 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.042 |  |
| 2026-07-03 00:04:46 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:04:12 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.043 |  |
| 2026-07-03 00:04:04 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.081 |  |
| 2026-07-03 00:04:01 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-03 00:03:34 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-07-03 00:02:50 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-03 00:02:46 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:02:25 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:02:25 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-07-03 00:02:20 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:02:15 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:01:52 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.169 |  |
| 2026-07-03 00:01:48 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:01:39 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:01:31 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-07-03 00:01:20 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:01:12 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:00:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-02 23:38:41 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-07-02 23:37:23 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-02 23:32:18 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 00:15:10 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-07-03 00:06:35 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-07-03 00:05:58 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-07-03 00:04:01 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-03 00:02:50 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-02 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:06:22 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:01:12 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:10:21 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-02 23:37:23 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:01:48 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:02:15 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-02 23:00:33 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:58 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:04:46 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:00:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:02:25 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:02:20 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:06:18 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:51:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 23:16:51 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:05:55 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:01:20 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:01:39 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-02 23:25:04 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.005 |  |
| 2026-07-02 23:32:18 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.008 |  |
| 2026-07-03 00:05:52 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-07-03 00:02:25 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-07-03 00:03:34 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-07-03 00:01:31 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-07-02 23:01:40 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.011 |  |
| 2026-07-02 20:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-07-02 23:38:41 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-07-02 23:08:00 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.037 |  |
| 2026-07-03 00:05:21 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.042 |  |
| 2026-07-03 00:04:12 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.043 |  |
| 2026-07-03 00:04:04 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.081 |  |
| 2026-07-03 00:01:52 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.169 |  |
| 2026-07-02 22:23:26 | Panadugama (Nilwala Ganga) | 0.57 | 🟢 Normal | -7.842 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)