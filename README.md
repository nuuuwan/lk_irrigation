# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_05:02:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,583 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 05:02:53 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.276 |  |
| 2026-08-02 05:02:43 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | -0.017 |  |
| 2026-08-02 05:02:34 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:02:31 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:02:09 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:01:45 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:01:45 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:01:42 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:01:39 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:01:02 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-02 04:44:23 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.037 |  |
| 2026-08-02 04:36:31 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.008 |  |
| 2026-08-02 04:30:32 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-02 04:27:07 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.017 |  |
| 2026-08-02 04:20:30 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 04:08:42 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-02 04:01:18 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 18:03:08 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 04:00:30 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:01:45 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:20:53 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:02:09 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:06:01 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:03:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:01:02 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-02 04:02:56 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-02 04:16:48 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:01:13 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:01:39 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:02:34 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:02:31 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-02 04:01:43 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 04:07:09 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:01:42 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-02 05:01:45 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-02 04:36:31 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.008 |  |
| 2026-08-02 04:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.011 |  |
| 2026-08-02 05:02:43 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | -0.017 |  |
| 2026-08-02 04:02:00 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.021 |  |
| 2026-08-02 04:20:30 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.023 |  |
| 2026-08-02 04:02:02 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.032 |  |
| 2026-08-02 04:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | -0.033 |  |
| 2026-08-02 04:44:23 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.037 |  |
| 2026-08-02 04:12:13 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.039 |  |
| 2026-08-02 04:06:05 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.039 |  |
| 2026-08-02 04:05:14 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.039 |  |
| 2026-08-01 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.042 |  |
| 2026-08-02 04:04:53 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.051 |  |
| 2026-08-02 04:11:13 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.057 |  |
| 2026-08-02 04:06:12 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | -0.075 |  |
| 2026-08-02 03:57:51 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.108 |  |
| 2026-08-02 04:04:57 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | -0.113 |  |
| 2026-08-02 04:01:48 | Ellagawa (Kalu Ganga) | 6.59 | 🟢 Normal | -0.114 |  |
| 2026-08-02 05:02:53 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.276 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)