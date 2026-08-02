# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_07:01:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,658 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 07:01:44 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:01:39 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 07:01:39 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | -0.161 |  |
| 2026-08-02 07:01:36 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:01:14 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:01:00 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:00:45 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-08-02 07:00:22 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-08-02 06:34:00 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 06:24:52 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-02 06:23:11 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.008 |  |
| 2026-08-02 06:19:56 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-02 06:15:52 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 06:03:19 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-02 06:00:25 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-02 06:01:25 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-02 06:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-02 06:11:29 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-02 07:01:39 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 07:00:45 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-08-02 06:11:57 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-02 06:03:11 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-02 06:01:32 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 06:01:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:01:00 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 06:34:00 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 06:19:56 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-02 06:24:52 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:01:13 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:01:44 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 06:13:17 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-02 06:05:08 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:01:36 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:01:14 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-02 06:23:11 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.008 |  |
| 2026-08-02 06:06:05 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-08-02 06:04:47 | Glencourse (Kelani Ganga) | 10.47 | 🟢 Normal | -0.010 |  |
| 2026-08-02 07:00:22 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-08-02 06:08:44 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-08-02 06:03:38 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-08-02 06:02:49 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.031 |  |
| 2026-08-02 06:03:39 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.037 |  |
| 2026-08-02 06:06:18 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.052 |  |
| 2026-08-02 06:01:43 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.053 |  |
| 2026-08-02 06:01:25 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.073 |  |
| 2026-08-02 06:04:31 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.083 |  |
| 2026-08-02 06:07:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.098 |  |
| 2026-08-02 07:01:39 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | -0.161 |  |
| 2026-08-02 06:02:48 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.164 |  |
| 2026-08-02 06:01:08 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | -0.200 |  |
| 2026-08-02 06:02:09 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | -0.405 |  |
| 2026-08-02 06:08:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -2.647 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)