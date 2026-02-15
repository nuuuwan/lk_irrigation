# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_13:10:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,739 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 13:10:18 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:09:31 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:08:48 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 13:08:03 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:07:22 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:07:22 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.028 |  |
| 2026-02-15 13:07:17 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-15 13:07:14 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.021 |  |
| 2026-02-15 13:07:12 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:05:37 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-02-15 13:05:33 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:05:10 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.15 | 🟢 Normal | -0.058 |  |
| 2026-02-15 13:04:56 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.191 |  |
| 2026-02-15 13:04:38 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.040 |  |
| 2026-02-15 13:03:39 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-02-15 13:03:31 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:03:28 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:03:23 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:03:22 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:03:12 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 13:03:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.051 |  |
| 2026-02-15 13:03:07 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-02-15 13:03:04 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:02:52 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 13:02:46 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-02-15 13:02:41 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-02-15 13:02:10 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:42 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:37 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-15 13:01:25 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:19 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:17 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:12 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:08 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:00:54 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2026-02-15 13:00:51 | Manampitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.051 |  |
| 2026-02-15 13:00:46 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-02-15 13:00:26 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:00:11 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | -0.130 |  |
| 2026-02-15 12:25:07 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 13:05:37 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-02-15 13:07:17 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-15 13:03:12 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 13:02:52 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 13:08:48 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 13:02:10 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:00:26 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:12 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:42 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:03:22 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:07:22 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:17 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:05:10 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:03:31 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:03:28 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:08 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:19 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:03:23 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:08:03 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:05:33 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:10:18 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:09:31 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:01:25 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 13:00:54 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2026-02-15 13:01:37 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-15 13:00:46 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-02-15 13:02:41 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-02-15 13:02:46 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-02-15 13:07:14 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.021 |  |
| 2026-02-15 13:03:07 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-02-15 13:07:22 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.028 |  |
| 2026-02-15 13:03:39 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-02-15 13:04:38 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.040 |  |
| 2026-02-15 13:00:51 | Manampitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.051 |  |
| 2026-02-15 13:03:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.051 |  |
| 2026-02-15 13:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.15 | 🟢 Normal | -0.058 |  |
| 2026-02-15 13:00:11 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | -0.130 |  |
| 2026-02-15 13:04:56 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.191 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)