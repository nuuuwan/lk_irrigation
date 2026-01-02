# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_22:46:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,974 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 22:46:44 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-02 22:15:24 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:11:04 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-02 22:08:24 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:07:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:07:36 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:07:34 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:07:31 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-02 22:07:05 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.058 |  |
| 2026-01-02 22:06:37 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:06:24 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:05:52 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-01-02 22:05:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-02 22:05:22 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-02 22:05:22 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-01-02 22:05:20 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:04:54 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:04:49 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:04:26 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:04:24 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:04:07 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 22:03:51 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.065 |  |
| 2026-01-02 22:03:41 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:03:30 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:03:24 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:03:15 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:03:08 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:02:54 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:02:42 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 22:02:33 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-01-02 22:02:27 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:02:22 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:02:08 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.031 |  |
| 2026-01-02 22:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:01:57 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:01:41 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:01:16 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-02 22:01:00 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 22:00:49 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 22:02:33 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-01-02 22:07:31 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-02 22:05:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-02 22:01:16 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-02 22:46:44 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-02 22:05:22 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-02 22:11:04 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-02 22:01:00 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 22:04:07 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 22:02:42 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 22:08:24 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:03:41 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:03:30 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:12 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:15:24 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:02:27 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:07:34 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:04:24 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:07:36 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:04:49 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:02:22 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:05:20 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:02:54 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:07:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:05:22 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-01-02 22:06:37 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:04:54 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:01:57 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:06:24 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:01:41 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:03:08 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:04:26 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-02 22:05:52 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-01-02 18:03:09 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-01-02 22:02:08 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.031 |  |
| 2026-01-02 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.33 | 🟢 Normal | -0.049 |  |
| 2026-01-02 22:07:05 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.058 |  |
| 2026-01-02 22:03:51 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)