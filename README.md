# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--04_09:28:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **88,808 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 09:28:09 | Horowpothana (Yan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:09:30 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-03-04 09:08:59 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:08:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-03-04 09:07:27 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:07:20 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:06:55 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-04 09:06:48 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:06:23 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:05:30 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:04:56 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:04:53 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-04 09:04:34 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:04:31 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.010 |  |
| 2026-03-04 09:04:22 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-04 09:04:09 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:03:45 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:03:31 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-03-04 09:03:30 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:03:19 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.049 |  |
| 2026-03-04 09:03:12 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.010 |  |
| 2026-03-04 09:03:07 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-04 09:03:03 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.103 |  |
| 2026-03-04 09:02:52 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:02:22 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-04 09:02:21 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:02:18 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:02:10 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.033 |  |
| 2026-03-04 09:02:01 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-03-04 09:01:58 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-04 09:01:55 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:01:30 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:01:30 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.053 |  |
| 2026-03-04 09:01:30 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:01:16 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.109 |  |
| 2026-03-04 09:00:51 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:00:35 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:00:28 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 09:02:01 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-03-04 09:01:58 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-04 09:02:22 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-04 09:03:07 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-04 09:02:52 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:04:34 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:01:55 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:02:18 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:28:09 | Horowpothana (Yan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:03:30 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:04:56 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:01:30 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:05:30 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:07:20 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:03:45 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:07:27 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:00:35 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:01:30 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:02:21 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:04:09 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:06:48 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:06:23 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:00:28 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:08:59 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-04 09:04:22 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-04 09:04:53 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-04 07:04:25 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-04 09:04:31 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.010 |  |
| 2026-03-04 09:06:55 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-04 09:03:12 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.010 |  |
| 2026-03-04 09:09:30 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-03-04 09:03:31 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-03-04 09:08:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-03-04 09:02:10 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.033 |  |
| 2026-03-04 09:03:19 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.049 |  |
| 2026-03-04 09:01:30 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.053 |  |
| 2026-03-04 09:03:03 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.103 |  |
| 2026-03-04 09:01:16 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)