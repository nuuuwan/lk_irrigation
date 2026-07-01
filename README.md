# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_00:20:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,780 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 00:20:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | -2.769 |  |
| 2026-07-02 00:20:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | -2.769 |  |
| 2026-07-02 00:17:36 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:15:40 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-02 00:15:01 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:08:03 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:07:52 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:07:32 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:07:09 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 00:06:39 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.039 |  |
| 2026-07-02 00:06:13 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:06:10 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:06:07 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:05:17 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.144 |  |
| 2026-07-02 00:04:27 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:04:07 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:04:06 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.012 |  |
| 2026-07-02 00:04:02 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-07-02 00:03:42 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-02 00:03:12 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 00:03:07 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-07-02 00:03:03 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:02:58 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -18.000 |  |
| 2026-07-02 00:02:56 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -18.000 |  |
| 2026-07-02 00:02:50 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-07-02 00:02:46 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-07-02 00:02:43 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:02:42 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | -0.031 |  |
| 2026-07-02 00:01:48 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:01:32 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:01:30 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:01:20 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:57:36 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 00:03:42 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-02 00:15:40 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-02 00:03:12 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 00:07:09 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 00:07:52 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:29 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:03:03 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:01:20 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:15:01 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:01:30 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:01:32 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:06:53 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:04:09 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:06:13 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:17:36 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:00:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:06:10 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:02:43 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:03:20 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:07:32 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:01:48 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:06:07 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:04:07 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:02 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:07:56 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:08:03 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:04:27 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:18:50 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-07-02 00:02:46 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-07-02 00:02:50 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-07-02 00:04:06 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.012 |  |
| 2026-07-02 00:03:07 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-07-02 00:04:02 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-07-02 00:02:42 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | -0.031 |  |
| 2026-07-02 00:06:39 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.039 |  |
| 2026-07-02 00:05:17 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.144 |  |
| 2026-07-01 22:04:59 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.186 |  |
| 2026-07-02 00:20:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | -2.769 |  |
| 2026-07-02 00:02:58 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)