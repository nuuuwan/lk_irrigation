# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_21:15:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **69,583 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 21:15:52 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:14:53 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:09:26 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:08:45 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-10 21:07:13 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:06:52 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-02-10 21:06:20 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-02-10 21:06:17 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.059 |  |
| 2026-02-10 21:05:40 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:05:38 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:05:16 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:05:14 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.019 |  |
| 2026-02-10 21:05:07 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:04:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.091 |  |
| 2026-02-10 21:04:10 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:03:44 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-02-10 21:03:36 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:03:33 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:03:24 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.068 |  |
| 2026-02-10 21:03:10 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:03:09 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:03:01 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:02:59 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:02:46 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:02:35 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:02:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:02:17 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:02:05 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-10 21:02:02 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.023 |  |
| 2026-02-10 21:01:57 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:01:57 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:01:11 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:00:55 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:00:37 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-02-10 21:00:33 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:00:18 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-02-10 20:25:16 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 21:00:18 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-02-10 21:06:52 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-02-10 18:04:12 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-10 21:00:55 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:09:26 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:02:59 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:14:53 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:03:01 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-10 18:03:04 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:15:52 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:04:10 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:03:36 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:02:02 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:01:57 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:03:41 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:07:13 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:00:33 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:02:17 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:03:10 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:05:40 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:05:07 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:03:33 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:02:46 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:01:11 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:03:09 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:05:16 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:25:16 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.008 |  |
| 2026-02-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-10 21:08:45 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-10 21:00:37 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-02-10 21:02:05 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-10 21:03:44 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-02-10 21:05:14 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.019 |  |
| 2026-02-10 21:06:20 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-02-10 21:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.023 |  |
| 2026-02-10 21:06:17 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.059 |  |
| 2026-02-10 21:03:24 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.068 |  |
| 2026-02-10 21:04:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)