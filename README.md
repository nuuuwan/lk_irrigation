# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_15:10:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,988 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 15:10:42 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:08:55 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-05-02 15:08:32 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:08:03 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:07:15 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.120 |  |
| 2026-05-02 15:06:56 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-02 15:06:45 | Kithulgala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.110 |  |
| 2026-05-02 15:06:18 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.005 |  |
| 2026-05-02 15:06:00 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-05-02 15:05:56 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-02 15:05:55 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:05:32 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:04:58 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.028 |  |
| 2026-05-02 15:04:58 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-02 15:04:55 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-02 15:04:45 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | -0.029 |  |
| 2026-05-02 15:04:38 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:04:37 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:04:25 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:04:11 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:03:54 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:03:23 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:03:18 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.012 |  |
| 2026-05-02 15:03:14 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-02 15:03:07 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-02 15:02:37 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:02:27 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-05-02 15:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | -0.020 |  |
| 2026-05-02 15:02:10 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 15:01:58 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.055 |  |
| 2026-05-02 15:01:51 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:01:51 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:01:37 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:01:33 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:01:28 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:01:14 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:01:05 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:00:19 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 15:04:55 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-02 15:03:07 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-02 14:00:41 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-02 15:03:14 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-02 15:04:58 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-02 15:06:56 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-02 15:02:10 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 15:01:51 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:01:05 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:01:14 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:03:54 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:08:32 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:04:37 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:04:11 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:03:23 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:01:51 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:04:38 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:05:55 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:04:25 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:10:42 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:05:32 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:01:37 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:08:03 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:01:33 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:01:28 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:06:18 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.005 |  |
| 2026-05-02 15:08:55 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-05-02 15:05:56 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-02 15:03:18 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.012 |  |
| 2026-05-02 15:06:00 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-05-02 15:02:27 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-05-02 15:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | -0.020 |  |
| 2026-05-02 15:04:58 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.028 |  |
| 2026-05-02 15:04:45 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | -0.029 |  |
| 2026-05-02 15:00:19 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.040 |  |
| 2026-05-02 15:01:58 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.055 |  |
| 2026-05-02 15:06:45 | Kithulgala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.110 |  |
| 2026-05-02 15:07:15 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)