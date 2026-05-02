# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_22:29:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,256 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 22:29:45 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-02 22:20:22 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:18:37 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-02 22:17:49 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:15:35 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:11:47 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.035 |  |
| 2026-05-02 22:10:38 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-02 22:10:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-02 22:08:28 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:08:24 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:07:26 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.091 |  |
| 2026-05-02 22:06:49 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-02 22:06:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:05:52 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:05:38 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-02 22:05:14 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:04:13 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-05-02 22:03:45 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-02 22:03:26 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.042 |  |
| 2026-05-02 22:03:19 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-05-02 22:02:42 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:02:34 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-02 22:02:27 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-05-02 22:02:25 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-05-02 22:02:18 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:02:15 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 22:01:33 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:01:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:01:30 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:01:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-05-02 22:00:41 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:00:30 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-02 22:00:27 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.043 |  |
| 2026-05-02 22:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 22:29:45 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-02 18:01:54 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-02 22:03:45 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-02 22:10:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-02 22:18:37 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-02 22:00:30 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-02 22:05:38 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-02 22:02:34 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-02 22:02:15 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 22:00:41 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:01:33 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:08:28 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:01:17 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:20:22 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:15:35 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:02:42 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:01:30 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:06:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:02:18 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:08:24 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:05:52 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:17:49 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:01:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:05:14 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:06:49 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-02 22:10:38 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:01:54 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-02 22:03:19 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-05-02 22:02:25 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-05-02 22:02:27 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-05-02 22:01:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-05-02 22:04:13 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-05-02 22:11:47 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.035 |  |
| 2026-05-02 22:03:26 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.042 |  |
| 2026-05-02 22:00:27 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.043 |  |
| 2026-05-02 22:07:26 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.091 |  |
| 2026-05-02 20:09:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)