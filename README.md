# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--02_18:29:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,386 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 18:29:13 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:12:44 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:11:14 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:10:40 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:08:17 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:08:16 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:07:20 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-02 18:06:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:06:00 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.146 |  |
| 2026-03-02 18:05:32 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:05:28 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-02 18:05:12 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:04:48 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:04:38 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:03:59 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:03:53 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 13.289 | 🔺 Rising |
| 2026-03-02 18:03:39 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.072 |  |
| 2026-03-02 18:03:39 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-03-02 18:03:36 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-02 18:03:14 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-03-02 18:03:06 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:03:04 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:02:53 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:02:44 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:02:43 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.149 |  |
| 2026-03-02 18:02:41 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:02:26 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:02:21 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.471 | 🔺 Rising |
| 2026-03-02 18:02:20 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:02:12 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-02 18:02:07 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:01:57 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-02 18:01:35 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.066 |  |
| 2026-03-02 18:01:35 | Rathnapura (Kalu Ganga) | 0.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-02 18:01:30 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:01:24 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 13.289 | 🔺 Rising |
| 2026-03-02 18:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:51 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 18:00:50 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:46 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:27 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:19 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 18:03:53 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 13.289 | 🔺 Rising |
| 2026-03-02 18:02:21 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.471 | 🔺 Rising |
| 2026-03-02 18:07:20 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-02 18:05:28 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-02 18:01:35 | Rathnapura (Kalu Ganga) | 0.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-02 18:00:51 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 18:00:27 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:02:20 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:02:41 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:19 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:46 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:02:53 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:03:06 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:03:04 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:01:30 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:05:32 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:29:13 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:12:44 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:03:59 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:50 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:08:16 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:04:48 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:04:38 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:02:07 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:11:14 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:02:44 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:10:40 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:06:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:03:36 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-02 18:01:57 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-02 18:02:12 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-02 18:03:14 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-03-02 18:03:39 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-03-02 17:02:42 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.041 |  |
| 2026-03-02 18:01:35 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.066 |  |
| 2026-03-02 18:03:39 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.072 |  |
| 2026-03-02 18:06:00 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.146 |  |
| 2026-03-02 18:02:43 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)