# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_02:22:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,502 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 02:22:16 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | -0.122 |  |
| 2026-08-02 02:18:46 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.013 |  |
| 2026-08-02 02:15:42 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:11:59 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:10:34 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:06:31 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:06:26 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | -0.172 |  |
| 2026-08-02 02:06:18 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.029 |  |
| 2026-08-02 02:05:47 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-08-02 02:05:21 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-08-02 02:05:11 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:04:20 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.070 |  |
| 2026-08-02 02:04:19 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:04:13 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 02:04:07 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-08-02 02:04:02 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-08-02 02:04:01 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.038 |  |
| 2026-08-02 02:03:53 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-08-02 02:03:25 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | -0.550 |  |
| 2026-08-02 02:03:14 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.005 |  |
| 2026-08-02 02:03:08 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-02 02:02:40 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:02:29 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:02:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.32 | 🟢 Normal | -0.025 |  |
| 2026-08-02 02:01:44 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:01:36 | Ellagawa (Kalu Ganga) | 6.83 | 🟢 Normal | -0.120 |  |
| 2026-08-02 02:01:11 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-08-02 02:00:57 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:00:49 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:00:11 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-02 01:57:58 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.550 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 02:04:07 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-08-01 23:18:00 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-02 02:03:08 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-02 02:04:13 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 18:03:08 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 02:01:44 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:00:57 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:00:49 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:02:29 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:04:57 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:05:11 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:03:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:06:44 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:06:31 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:11:42 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:01:13 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:00:11 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:02:40 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:11:59 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:15:42 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:04:19 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:10:34 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 02:03:14 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.005 |  |
| 2026-08-02 01:04:27 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-08-02 02:01:11 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-08-02 02:18:46 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.013 |  |
| 2026-08-02 02:05:47 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-08-02 02:05:21 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-08-02 02:04:02 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-08-02 02:02:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.32 | 🟢 Normal | -0.025 |  |
| 2026-08-02 02:06:18 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.029 |  |
| 2026-08-02 02:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-08-02 02:04:01 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.038 |  |
| 2026-08-01 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.042 |  |
| 2026-08-02 02:04:20 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.070 |  |
| 2026-08-02 02:01:36 | Ellagawa (Kalu Ganga) | 6.83 | 🟢 Normal | -0.120 |  |
| 2026-08-02 02:22:16 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | -0.122 |  |
| 2026-08-02 02:06:26 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | -0.172 |  |
| 2026-08-02 02:03:25 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | -0.550 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)