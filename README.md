# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--16_13:22:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,626 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 13:22:18 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.007 |  |
| 2026-02-16 13:17:40 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 5.688 | 🔺 Rising |
| 2026-02-16 13:11:56 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:11:02 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:10:20 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:10:03 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-02-16 13:09:37 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:09:20 | Thawalama (Gin Ganga) | 0.23 | 🟢 Normal | 5.688 | 🔺 Rising |
| 2026-02-16 13:07:51 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.018 |  |
| 2026-02-16 13:07:20 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-02-16 13:07:18 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:06:10 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:06:09 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-16 13:05:14 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:05:09 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-16 13:04:41 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-16 13:04:35 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:04:35 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:03:46 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-16 13:03:36 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:03:29 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 13:02:47 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:02:41 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:02:39 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-16 13:02:39 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:02:14 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-16 13:02:14 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-02-16 13:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-16 13:02:02 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-16 13:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-16 13:01:31 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.021 |  |
| 2026-02-16 13:01:15 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:01:13 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:01:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:00:55 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:00:53 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:00:40 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.208 |  |
| 2026-02-16 13:00:39 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.024 |  |
| 2026-02-16 13:00:24 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 13:17:40 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 5.688 | 🔺 Rising |
| 2026-02-16 13:10:03 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-02-16 13:05:09 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-16 13:06:09 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-16 13:02:39 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-16 13:04:41 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-16 13:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-16 13:03:29 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 13:02:41 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:04:35 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:11:02 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:02:39 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:04:35 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:05:14 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-16 12:08:43 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:03:36 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:01:15 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:11:56 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:00:55 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:00:53 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:09:37 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:01:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:07:18 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:06:10 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:01:13 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:02:47 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:22:18 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.007 |  |
| 2026-02-16 13:07:20 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-02-16 13:03:46 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-16 13:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-16 13:02:02 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-16 13:02:14 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-16 13:07:51 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.018 |  |
| 2026-02-16 13:01:31 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.021 |  |
| 2026-02-16 13:00:24 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-02-16 12:04:53 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-02-16 13:00:39 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.024 |  |
| 2026-02-16 13:02:14 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-02-16 13:00:40 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.208 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)