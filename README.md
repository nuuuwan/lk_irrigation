# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_18:28:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,825 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 18:28:04 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:27:35 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-02 18:19:17 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-01-02 18:10:30 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-02 18:08:42 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:06:22 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.057 |  |
| 2026-01-02 18:05:58 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-01-02 18:05:50 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:05:42 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-01-02 18:05:12 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-02 18:05:01 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:04:47 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-02 18:04:28 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-02 18:04:12 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-02 18:04:11 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:04:00 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:03:58 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:03:35 | Horowpothana (Yan Oya) | 2.81 | 🟢 Normal | -0.038 |  |
| 2026-01-02 18:03:34 | Siyambalanduwa (Heda Oya) | 1.23 | 🟢 Normal | -0.029 |  |
| 2026-01-02 18:03:33 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.042 |  |
| 2026-01-02 18:03:09 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-01-02 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.33 | 🟢 Normal | -0.049 |  |
| 2026-01-02 18:03:08 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:59 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:46 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.080 |  |
| 2026-01-02 18:02:38 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.060 |  |
| 2026-01-02 18:02:12 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:11 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-01-02 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-01-02 18:02:09 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:01:53 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-02 18:01:27 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-01-02 18:01:21 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:01:11 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-01-02 18:00:49 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-02 18:00:46 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:00:30 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-02 18:00:11 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.040 |  |
| 2026-01-02 17:58:01 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 18:10:30 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-02 18:00:30 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-02 18:04:47 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-02 18:05:12 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-02 18:27:35 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-02 18:04:12 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-02 18:02:09 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:05:01 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:12 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:04:00 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:08:42 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:59 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:03:08 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:05:50 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:00:46 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:28:04 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:04:11 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:03:58 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:01:21 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:05:42 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-01-02 18:04:28 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-02 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-01-02 18:00:49 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-02 18:01:53 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-02 18:01:27 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-01-02 18:19:17 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-01-02 18:03:09 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-01-02 18:02:11 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-01-02 18:03:34 | Siyambalanduwa (Heda Oya) | 1.23 | 🟢 Normal | -0.029 |  |
| 2026-01-02 18:01:11 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-01-02 18:03:35 | Horowpothana (Yan Oya) | 2.81 | 🟢 Normal | -0.038 |  |
| 2026-01-02 18:00:11 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.040 |  |
| 2026-01-02 18:03:33 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.042 |  |
| 2026-01-02 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.33 | 🟢 Normal | -0.049 |  |
| 2026-01-02 18:05:58 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-01-02 18:06:22 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.057 |  |
| 2026-01-02 18:02:38 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.060 |  |
| 2026-01-02 18:02:46 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)