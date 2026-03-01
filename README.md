# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--02_03:22:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **86,793 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 03:22:34 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:16:39 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:14:07 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.028 |  |
| 2026-03-02 03:13:17 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:11:04 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:09:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.064 |  |
| 2026-03-02 03:08:06 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-02 03:07:19 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.015 |  |
| 2026-03-02 03:06:58 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:06:32 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:06:15 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:05:45 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-03-02 03:05:08 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-02 03:05:02 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:04:57 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:04:48 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:04:32 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.072 |  |
| 2026-03-02 03:03:14 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:03:12 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-03-02 03:03:12 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:03:04 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:02:51 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 34.615 | 🔺 Rising |
| 2026-03-02 03:02:26 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:02:25 | Pitabeddara (Nilwala Ganga) | 0.00 | 🟢 Normal | 34.615 | 🔺 Rising |
| 2026-03-02 03:02:24 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 34.615 | 🔺 Rising |
| 2026-03-02 03:02:23 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 34.615 | 🔺 Rising |
| 2026-03-02 03:02:20 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-03-02 03:01:42 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.117 |  |
| 2026-03-02 03:01:38 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:01:35 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:01:27 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-02 03:01:09 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-03-02 03:00:39 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:00:15 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-02 02:53:53 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 02:51:49 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 02:39:42 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.072 |  |
| 2026-03-02 02:38:17 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 03:02:51 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 34.615 | 🔺 Rising |
| 2026-03-02 01:28:50 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.767 | 🔺 Rising |
| 2026-03-02 03:03:12 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-03-02 03:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-03-01 18:01:43 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-02 03:01:27 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-02 03:00:15 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-02 03:08:06 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-02 03:02:26 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:06:15 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:22:34 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-02 01:03:40 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 18:01:07 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:04:48 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:05:02 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:11:04 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:01:38 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:06:58 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-02 02:05:43 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:03:14 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:03:04 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:02:20 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:04:57 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:16:39 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:01:35 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 02:01:37 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:13:17 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:06:32 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:03:12 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-02 03:05:45 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-03-02 03:05:08 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-02 03:01:09 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-03-01 18:00:31 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-02 03:07:19 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.015 |  |
| 2026-03-02 03:14:07 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.028 |  |
| 2026-03-02 03:09:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.064 |  |
| 2026-03-02 03:04:32 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.072 |  |
| 2026-03-02 03:01:42 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.117 |  |
| 2026-03-01 23:03:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.717 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)