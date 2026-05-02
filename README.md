# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_07:19:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,664 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 07:19:36 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:13:15 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-02 07:12:18 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-02 07:10:03 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:09:32 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-05-02 07:08:29 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.028 |  |
| 2026-05-02 07:08:13 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 07:08:06 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.064 |  |
| 2026-05-02 07:07:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-02 07:07:15 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-02 07:06:22 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-02 07:06:22 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.201 |  |
| 2026-05-02 07:06:11 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.022 |  |
| 2026-05-02 07:05:15 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:05:11 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:05:07 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-05-02 07:05:01 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.022 |  |
| 2026-05-02 07:04:30 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-02 07:04:24 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.047 |  |
| 2026-05-02 07:04:00 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-02 07:03:46 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.029 |  |
| 2026-05-02 07:03:09 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:03:02 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-02 07:02:10 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:02:09 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-05-02 07:01:49 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-05-02 07:01:45 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-02 07:01:42 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:01:34 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:01:31 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.010 |  |
| 2026-05-02 07:01:16 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-02 07:01:14 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:00:48 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.067 |  |
| 2026-05-02 07:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:00:08 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 06:36:20 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 07:07:15 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-02 07:13:15 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-02 07:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-02 07:04:00 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-02 07:07:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-02 07:06:22 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-02 06:14:28 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-02 07:12:18 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-02 07:00:08 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 07:08:13 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 07:19:36 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:06:11 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:02:10 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:01:34 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:10:03 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:05:15 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:08:05 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:03:09 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:01:14 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:05:11 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:05:07 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-05-02 07:01:31 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.010 |  |
| 2026-05-02 07:01:16 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-02 07:04:30 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-02 07:01:45 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-02 07:01:49 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-05-02 07:09:32 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-05-02 07:06:11 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.022 |  |
| 2026-05-02 07:05:01 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.022 |  |
| 2026-05-02 07:08:29 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.028 |  |
| 2026-05-02 07:03:46 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.029 |  |
| 2026-05-02 07:02:09 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-05-01 18:00:26 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-05-02 07:04:24 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.047 |  |
| 2026-05-02 07:08:06 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.064 |  |
| 2026-05-02 07:00:48 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.067 |  |
| 2026-05-02 06:10:18 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.075 |  |
| 2026-05-02 07:06:22 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)